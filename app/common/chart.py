def get_pie_chart(data, colors, search, dict_lable, label):
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
                "name": f"Number of {search}",
                "values": last_val,
            },
        },
        "colors": colors,
        "percent": percent,
    }
