import requests

def download_file(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text.splitlines()

def split_file(lines):
    half = len(lines) // 2
    return lines[:half], lines[half:]

def save_file(filename, lines):
    with open(filename, 'w') as file:
        file.write('\n'.join(lines))

def main():
    url = 'https://big.oisd.nl/domainswild2'
    lines = download_file(url)
    part1, part2 = split_file(lines)
    save_file('dns_wild_1.dns', part1)
    save_file('dns_wild_2.dns', part2)

if __name__ == "__main__":
    main()
