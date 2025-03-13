import equibasecarddaily

import equibasethoroughbredhorsesdaily

import equibasejockeysdaily

import equibasetrainersdaily

import equibaseownersdaily

import equibaserunnerinfoextract

import equibaserunnerinfoparse

def scheduled():

    equibasecarddaily.equibasecard()

    equibasethoroughbredhorsesdaily.equibasethoroughbredhorsesdaily()

    equibasejockeysdaily.equibasejockeysdaily()

    equibasetrainersdaily.equibasetrainersdaily()

    equibaseownersdaily.equibaseownersdaily()

    equibaserunnerinfoextract.equibaserunnerinfoextract()

    equibaserunnerinfoparse.equibaserunnerinfoparse()


if __name__ == '__main__':

    scheduled()