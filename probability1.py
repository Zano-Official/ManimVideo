#encoding:utf-8
from re import S
from tkinter import font
from turtle import color, position, update
from typing_extensions import runtime
from pyparsing import White
from manimlib import *

class Lesson(Scene):
    def construct(self):
        title = Text("随机事件与概率", font="微软雅黑", font_size=50,color=BLUE)
        lesson = Text('有限样本空间与随机事件',font="微软雅黑",font_size=75,color=GREEN)
        title.move_to(UP*2)
        self.play(Write(title),runtime=0.1)
        self.play(Write(lesson),runtime=0.1)
        self.wait(1)
        knowledge1 = Text("知识点一 随机试验和样本空间", font="微软雅黑", font_size=25,color=BLUE) # np.array([3,-3,0])   ,position=UP*3+LEFT*-3
        part1 = Text('1.随机试验的概念和特点',font="微软雅黑",font_size=30,color=GREEN) # np.array([2.5,-2.5,0])   ,position=UP*2.5+LEFT*-2.5
        knowledge1.move_to(UP*3.5+LEFT*4.5) #   np.array([3,-3,0])
        part1.move_to(UP*3+LEFT*4.5) #   np.array([2.5,-3,0])
        #knowledge.set_sheen(0.5,DOWN)
        #knowledge.set_color([BLUE,GREEN])
        #part.set_sheen(0.5,UP)
        #part.set_color([BLUE,GREEN])
        self.play(FadeTransform(title,knowledge1),runtime=0.1)
        self.play(FadeTransform(lesson,part1),runtime=0.1)
        text1=Text(
            '(1)随机试验:我们把对__________的实现和对它的观察称为随机试验,常用字母___表示;\n \n'\
            '(2)随机试验的特点：\n'\
            '①试验可以在相同条件下______进行;\n'\
            '②试验的所有可能结果是__________的,并且不止一个;\n'\
            '③每次试验总是恰好出现这些可能结果中的一个,但事先不能确定出现哪一个结果.',
            font_size=42,font='微软雅黑')
        self.play(Write(text1),runtime=0.1)
        self.wait(3)
        text2 = Text(
            '(1)随机试验:我们把对 随机现象 的实现和对它的观察称为随机试验,常用字母 E 表示;\n \n'\
            '(2)随机试验的特点：\n'\
            '①试验可以在相同条件下 重复 进行;\n'\
            '②试验的所有可能结果是 明确可知 的,并且不止一个;\n'\
            '③每次试验总是恰好出现这些可能结果中的一个,但事先不能确定出现哪一个结果.',
            font="微软雅黑", font_size=42,
            t2c={" 随机现象 ": RED, " E ": RED, " 重复 ": RED ," 明确可知 ":RED}
        )
        self.play(FadeTransform(text1,text2),runtime=0.1)
        self.wait(2)
        self.play(FadeOut(text2,runtime=0.1))
        #self.play(FadeOutToPoint(UP*4+LEFT*5),runtime=0.1)
        #part.move_to(UP*0.5)
        #self.play(part,runtime=0.1)
        part2 = Text('2.样本点和样本空间',font="微软雅黑",font_size=30,color=GREEN)
        part2.move_to(UP*3+LEFT*4.5)
        self.play(FadeTransform(part1,part2),runtime=0.1)
        size=40
        list=[
            [Text('',font='微软雅黑',font_size=size),Text('定义',font='微软雅黑',font_size=size),Text('字母表示',font='微软雅黑',font_size=size)],
            [Text('样本点',font='微软雅黑',font_size=size),Text('我们把随机试验E的每个______\n的__________称为样本点',font='微软雅黑',font_size=size),Text('用___表示\n样本点',font='微软雅黑',font_size=size)],
            [Text('样本空间',font='微软雅黑',font_size=size),Text('全体________的集合\n称为试验E的样本空间',font='微软雅黑',font_size=size),Text('用___表示\n样本空间',font='微软雅黑',font_size=size)],
            [Text('有限样本空间',font='微软雅黑',font_size=size),Text('如果一个随机试验有n个\n可能结果ω1,ω2,…,ωn,则称\n样本空间Ω={ω1,ω2,…,ωn}\n为有限样本空间',font='微软雅黑',font_size=size),Text('Ω＝{ω1,ω2,…,ωn}',font='微软雅黑',font_size=size)]
        ]
        new_list=[
            [Text('',font='微软雅黑',font_size=size),Text('定义',font='微软雅黑',font_size=size),Text('字母表示',font='微软雅黑',font_size=size)],
            [Text('样本点',font='微软雅黑',font_size=size),Text('我们把随机试验E的每个 可能 \n的 基本结果 称为样本点',t2c={' 可能 ':RED,' 基本结果 ':RED},font='微软雅黑',font_size=size),Text('用 ω 表示\n样本点',t2c={' ω ':RED},font='微软雅黑',font_size=size)],
            [Text('样本空间',font='微软雅黑',font_size=size),Text('全体 样本点 的集合\n称为试验E的样本空间',t2c={' 样本点 ':RED},font='微软雅黑',font_size=size),Text('用 Ω 表示\n样本空间',t2c={' Ω ':RED},font='微软雅黑',font_size=size)],
            [Text('有限样本空间',font='微软雅黑',font_size=size),Text('如果一个随机试验有n个\n可能结果ω1,ω2,…,ωn,则称\n样本空间Ω={ω1,ω2,…,ωn}\n为有限样本空间',font='微软雅黑',font_size=size),Text('Ω＝{ω1,ω2,…,ωn}',font='微软雅黑',font_size=size)]
        ]
        for i in range(-1,3):
            for j in range(-1,2):
                #print(str(i)+','+str(j))
                list[i+1][j+1].move_to(UP*i*-1.5+UP+RIGHT*j*4.5)
                self.play(Write(list[i+1][j+1]),runtime=0.1)
        self.wait(3)
        for i in range(-1,3):
            for j in range(-1,2):
                new_list[i+1][j+1].move_to(UP*i*-1.5+UP+RIGHT*j*4.5)
                if new_list[i+1][j+1] != list[i+1][j+1]:
                    self.play(FadeTransform(list[i+1][j+1],new_list[i+1][j+1]),runtime=0.1)
        self.wait(2)
        for i in range(-1,3):
            for j in range(-1,2):
                if new_list[i+1][j+1] != list[i+1][j+1]:
                    self.play(FadeOut(new_list[i+1][j+1]),runtime=0)
                else:
                    self.play(FadeOut(list[i+1][j+1]),runtime=0)
        #self.play(FadeOut(knowledge1))
        part3=Text('对样本点和样本空间的再理解',font="微软雅黑",font_size=45,color=GREEN)
        part3.move_to(UP*2)
        self.play(FadeTransformPieces(part2,part3))
        text3=Text('(1)样本点是指随机试验的每个可能的基本结果,全体样本点的集合称为试验的样本空间;\n\n(2)只讨论样本空间为有限集的情况,即有限样本空间.',font="微软雅黑",font_size=42)
        self.play(FadeIn(text3))
        self.wait(2)
        self.play(FadeOut(text3))
        knowledge2=Text("知识点二 三种事件的定义", font="微软雅黑", font_size=25,color=BLUE)
        knowledge2.move_to(UP*3.5+LEFT*4.5)
        #part4 = Text('1.随机试验的概念和特点',font="微软雅黑",font_size=30,color=GREEN)
        #part4.move_to(UP*3+LEFT*4.5)
        #self.play(FadeTransform(part3,part4))
        self.play(FadeOut(part3))
        self.play(FadeTransform(knowledge1,knowledge2))
        size=35
        list=[
            Text('  随机事件:\n 我们将样本空间Ω的______称为随机事件,简称事件,并把只包含______样本点的事件称为基本事件,随机事件一般用大写字母A,B,C,…表示.在每次试验中,当且仅当A中某个样本点出现时,称为事件A发生',font='微软雅黑',font_size=size),
            Text('  必然事件:\n Ω作为自身的子集,包含了______的样本点,在每次试验中总有一个样本点发生,所以Ω总会发生,我们称Ω为必然事件',font='微软雅黑',font_size=size),
            Text('  不可能事件:\n 空集∅不包含______样本点,在每次试验中都不会发生,我们称∅为不可能事件',font='微软雅黑',font_size=size)
        ]
        new_list=[
            Text('  随机事件:\n 我们将样本空间Ω的 子集 称为随机事件,简称事件,并把只包含 一个 样本点的事件称为基本事件,随机事件一般用大写字母A,B,C,…表示.在每次试验中,当且仅当A中某个样本点出现时,称为事件A发生',t2c={' 子集 ':RED,' 一个 ':RED},font='微软雅黑',font_size=size),
            Text('  必然事件:\n Ω作为自身的子集,包含了 所有 的样本点,在每次试验中总有一个样本点发生,所以Ω总会发生,我们称Ω为必然事件',t2c={' 所有 ':RED},font='微软雅黑',font_size=size),
            Text('  不可能事件:\n 空集∅不包含 任何 样本点,在每次试验中都不会发生,我们称∅为不可能事件                                ',t2c={' 任何 ':RED},font='微软雅黑',font_size=size)
        ]
        for i in range(0,3):
            list[i].move_to(UP*(i*-2)+UP*2)
            self.play(Write(list[i]),runtime=0)
            new_list[i].move_to(UP*(i*-2)+UP*2)
        self.wait(3)
        for i in range(0,3):
            self.play(FadeTransform(list[i],new_list[i]),runtime=0)
        self.wait(2)
        for i in range(0,3):
            self.play(FadeOut(new_list[i]),runtime=0)
        part4=Text('判断一类事件是哪类事件的方法',font="微软雅黑",font_size=45,color=GREEN)
        part4.move_to(UP*2)
        text4=Text('一看条件，因为三种事件都是相对于一定条件而言的;\n二看结果是否发生,一定发生的是必然事件,不一定发生的是随机事件,一定不发生的是不可能事件.',font="微软雅黑",font_size=42)
        self.play(Write(part4))
        self.play(Write(text4))
        self.wait(3)
        part5=Text('写样本空间的关键是找样本点，具体有三种方法',font="微软雅黑",font_size=45,color=GREEN)
        part5.move_to(UP*2.5)
        text5=Text('(1)列举法:适用于样本点个数不是很多,可以把样本点一一列举出来的情况,但列举时必须按一定的顺序,要做到不重不漏;\n\n(2)列表法:适用于试验中包含两个或两个以上的元素,且试验结果相对较多的样本点个数的求解问题,通常把样本归纳为“有序实数对”,也可用坐标法,列表法的优点是准确、全面、不易遗漏;\n\n\n(3)树状图法:适用于较复杂问题中的样本点的探求，一般需要分步(两步及两步以上)完成的结果可以用树状图进行列举.',font="微软雅黑",font_size=42)
        self.play(FadeTransform(part4,part5))
        self.play(FadeTransform(text4,text5))
        self.wait(4)