def read_ids():
    with open("ids.txt") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content

def write_ids(id_list):
    with open("ids.txt", "w") as f:
        for ids in id_list:
            f.write("%s\n" %ids)

hn_posts_ids = read_ids()
