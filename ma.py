from parsers import Parser


def main():
    pars = Parser(
        'https://metalarea.org/forum/index.php?showforum=2&prune_day=60&sort_by=Z-A&sort_key=start_date&topicfilter=all&desc_filter=&desc_filter_opt=&st=50',
        'new.txt')
    pars.get_html()
    pars.parsing()


if __name__ == '__main__':
    main()
