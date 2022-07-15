import requests
import json

class ReleaseTable(object):
    def __init__(self, release):
        self.release = release
        self.width = 0
        self.total_downloads = 0
        self.repr_data = None

    def __repr__(self):
        if self.repr_data is None:
            self.parse_and_format()

        return self.repr_data

    def parse_and_format(self):
        rv = [ ]
        width = 0
    
        def append_to_rv(s=""):
            nonlocal width
            rv.append(s)
            width = max(width, len(s))

        release = self.release

        name = release["name"]
        tag_name = release["tag_name"]

        append_to_rv(f"Name: {name}")
        append_to_rv(f"Tag: {tag_name}")
        append_to_rv()

        append_to_rv("Assets:")
        assets = release["assets"]

        def format_assets(assets):
            l = [ ]
            tcount = 0

            for i, asset in enumerate(assets):
                name = asset["name"]
                download_count = asset["download_count"]
                tcount += download_count

                l.append((f"{i + 1}.", name, str(download_count)))

            l.append(('', "Total", str(tcount)))

            len_width = max([ len(i[0]) for i in l ])
            name_width = max([ len(i[1]) for i in l ])
            dcount_width = max([ len(i[2]) for i in l ])
                
            format_asset = f"{{:<{len_width}}} {{:<{name_width}}}\t{{:<{dcount_width}}}"

            rv = [ format_asset.format(i, name, dcount) for i, name, dcount in l ]

            self.total_downloads = tcount

            return rv

        for i in format_assets(assets):
            append_to_rv(i)

        width += 1
        append_to_rv("-" * width)
        self.width = width

        self.repr_data = "\n".join(rv)

def main():
    url = "https://api.github.com/repos/WretchedTeam/WintermuteV3/releases"

    response = requests.get(url)
    response.raise_for_status()

    releases = json.loads(response.content)

    overall_download_count = 0 

    for release in releases:
        r = ReleaseTable(release)
        r.parse_and_format()

        overall_download_count += r.total_downloads
        print(r)

    print(f"Overall Downloads: {overall_download_count}")

if __name__ == "__main__":
    main()

