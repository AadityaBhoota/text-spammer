import functions


def main():
    site = 'https://web.njit.edu/~cm395/theBeeMovieScript/'
    tagtoFind = 'pre'
    list = functions.accessSite(site, tagtoFind)
    functions.sendWords(list)


if __name__ == "__main__":
    main()
