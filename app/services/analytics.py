from datetime import datetime, timedelta


def get_range(period):
    t0 = datetime.strptime(((datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d 17:00:00")),
                           "%Y-%m-%d %H:%M:%S").strftime("%s")
    t7_0 = datetime.strptime(((datetime.today() - timedelta(days=7)).strftime("%Y-%m-%d 17:00:00")),
                             "%Y-%m-%d %H:%M:%S").strftime("%s")
    t30_0 = datetime.strptime(((datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d 17:00:00")),
                              "%Y-%m-%d %H:%M:%S").strftime("%s")
    t365_0 = datetime.strptime(((datetime.today() - timedelta(days=365)).strftime("%Y-%m-%d 17:00:00")),
                               "%Y-%m-%d %H:%M:%S").strftime("%s")
    t1 = datetime.strptime(((datetime.today()).strftime("%Y-%m-%d 17:00:00")), "%Y-%m-%d %H:%M:%S").strftime("%s")
    time = {
        'Today': 'range(start:' + t0 + ',stop:' + t1 + ')',
        'Last Week': 'range(start:' + t7_0 + ',stop:' + t1 + ')',
        'Last Month': 'range(start:' + t30_0 + ',stop:' + t1 + ')',
        'Last Year': 'range(start:' + t365_0 + ',stop:' + t1 + ')',
    }
    if period not in time.keys():
        return f"range(start:{period.split(';')[0]}T00:00:00.000Z,stop:{period.split(';')[1]}T23:59:59.000Z)"
    return time.get(period)


def return_query_edge(edge_ids):
    if edge_ids:
        edge = f"""|> filter(fn: (r) => r.edge_id =~ /{edge_ids}/ )"""
    else:
        edge = f""""""
    return edge
