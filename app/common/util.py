from app.common.database import SessionLocal


def validate_unique(table, field, **kwargs):
    session = SessionLocal()
    q = session.query(getattr(table, field)).filter_by(**kwargs).scalar()
    session.close()
    if q:
        raise ValueError(f"""Table {table.__name__} {field} already exist""")
    return kwargs[field]


def get_chart(data, search, dict_lable, label):
    labels = [dict_lable[i[search]] if i[search] else "" for i in data]
    values = [item["count"] for item in data]
    last_val = []
    for i in label:
        if i in labels:
            index_label = labels.index(i)
            last_val.append(values[index_label])
        else:
            last_val.append(0)
    percent = []
    for i in last_val:
        if sum(last_val) != 0:
            percent.append((i / sum(last_val)) * 100)
        else:
            percent.append(0)

    return {
        "type": "pie",
        "data": {
            "labels": label,
            "datasets": {
                "name": "Number of Vehicles",
                "values": last_val,
            },
        },
        "colors": ["#0072DB", "#469BFF", "#AAAFC7", "#50CC65"],
        "percent": percent,
    }
