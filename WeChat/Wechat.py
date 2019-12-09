# -*- coding: utf-8 -*-
# author: ZJendex
# place: Boston Amherst
# last update:  12/8/2019
import itchat
import matplotlib.pyplot as plt



def main():
    itchat.login()

    friends = itchat.get_friends()[1:]
    male = 0
    female = 0
    friend_province = []
    for index, friend in enumerate(friends):
        if friend['Sex'] == 1:
            male += 1
        if friend['Sex'] == 2:
            female += 1
        if friend['Province'] not in friend_province:
            friend_province.append(friend['Province'])

    friend_provinceNum = [0] * len(friend_province)

    for friend in friends:
        friend_provinceNum[friend_province.index(friend['Province'])] += 1

    print(friend_province)
    print(friend_provinceNum)
    for checker in friend_provinceNum[:]:
        if checker < 5:
            friend_province.pop(friend_provinceNum.index(checker))
            friend_provinceNum.pop(friend_provinceNum.index(checker))
            friend_provinceNum[friend_province.index('')] += 1
    
    #Delete the friends who didn't sign their location
    # empt_n = friend_province.index('')
    # friend_province.pop(empt_n)
    # friend_provinceNum.pop(empt_n)

    friend_province[friend_province.index('')] = '其他'

    # First Pie chart for people's location
    labels = friend_province
    sizes = friend_provinceNum

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)

    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig('Province Comparision.png')

    # Second Pie chart for sex of friends
    labels = 'male', 'female'
    sizes = [male, female]
    explode = (0, 0.1)  # only "explode" the 2nd slice

    fig2, ax2 = plt.subplots()
    ax2.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)

    ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.savefig('Sexual Proportion.png')

    print('Save completed')
    plt.show()


if __name__ == '__main__':
    main()

