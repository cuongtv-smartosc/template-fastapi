import os
import argparse

import pymysql

from app.config.settings import EnvDB


class ScriptRunner:

    def __init__(self, connection, delimiter=";", autocommit=True):
        self.connection = connection
        self.delimiter = delimiter
        self.autocommit = autocommit

    def run_script(self, sql):
        try:
            script = ""
            for line in sql.splitlines():
                strip_line = line.strip()
                if "DELIMITER $$" in strip_line:
                    self.delimiter = "$$"
                    continue
                if "DELIMITER ;" in strip_line:
                    self.delimiter = ";"
                    continue

                if strip_line and not strip_line.startswith("//") and not strip_line.startswith("--"):
                    script += line + "\n"
                    if strip_line.endswith(self.delimiter):
                        if self.delimiter == "$$":
                            script = script[:-1].rstrip("$") + ";"
                        cursor = self.connection.cursor()
                        cursor.execute(script)
                        script = ""

            if script.strip():
                raise Exception("Line missing end-of-line terminator (" + self.delimiter + ") => " + script)

            if not self.connection.get_autocommit():
                self.connection.commit()
        except Exception:
            if not self.connection.get_autocommit():
                self.connection.rollback()
            raise


if __name__ == '__main__':
    connection = pymysql.connect(host=EnvDB.DB_HOST, user="root", password=EnvDB.DB_PASS, autocommit=True)
    parser = argparse.ArgumentParser()
    parser.add_argument("-dir", "--dir_file", help="path file argument.")
    args = parser.parse_args()
    if args.dir_file:
        print("process import data...")
        # dir_file = os.path.dirname(os.path.abspath(__file__))
        file = open(args.dir_file)
        sql = file.read()
        ScriptRunner(connection).run_script(sql)
        print("close import data")
