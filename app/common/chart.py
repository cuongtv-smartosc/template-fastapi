def get_pie_chart(data, search, dict_lable, label):
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
    if search == "sale_type":
        colors = ["#0072DB", "#469BFF", "#AAAFC7", "#50CC65"]
    else:
        colors = [
            "#469BFF",
            "rgba(70, 155, 255, 0.7)",
            "#AAAFC7",
            "#FFC459",
            "#FC6563",
            "rgba(80, 204, 101, 0.7)",
        ]
    return {
        "type": "pie",
        "data": {
            "labels": label,
            "datasets": {
                "name": "Number of Vehicles",
                "values": last_val,
            },
        },
        "colors": colors,
        "percent": percent,
    }
