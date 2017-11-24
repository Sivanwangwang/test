######
#新建一个数据框
library(ggplot2)
x <- c('A','B','C','D','E','A') 
y <- c(13,22,16,31,8,9)
labs<-c("A\nB","A\nB","A\nB","A\nB","A\nB","A\nB")
df <- data.frame(x= x, y = y,labs=labs)

p=ggplot(data = df, mapping = aes(x = x)) + geom_bar()    #映射只有x=x时，默认的stat="count"，y=..count..
p=ggplot(data = df, mapping = aes(x = x,y=..count..)) + geom_bar(stat = "count")
p=ggplot(data = df, mapping = aes(x = x,y=..density..)) + geom_bar(stat = "count")#报错？？？



p=ggplot(data = df, mapping = aes(x = x, y = y)) + geom_bar(stat= 'identity')
p=ggplot(data = df, mapping = aes(x = x, y = y)) + geom_bar(stat= 'identity',fill="transparent",color="black")
p=ggplot(data = df, mapping = aes(x = x, y = y)) + geom_bar(stat= 'identity',fill="transparent",color="black",position = "dodge")



df<-barplottest
df$x<-as.numeric(df$x)
#write.csv(df,file="barplottest1.csv")
p=p+scale_x_continuous(breaks=1:5,labels = labs)
labs<-c("0\n开始","A","1","B","2","C","3","D","4","E","5")
p=p+scale_x_continuous(limits=c(0,5),breaks=seq(0,5,0.5)+0.2,labels = c(paste("0\n开始"),"A","1","B","2","C","3","D","4","E","5"))
p=p+scale_x_continuous(limits=c(0,5),breaks=seq(0,5,0.5)+0.2,labels = c(paste(bold("0")),"A","1","B","2","C","3","D","4","E","5"))
p=p+scale_x_continuous(limits=c(0,5),breaks=seq(0,5,0.5)+0.2,labels = labs)

p=p+coord_flip()


######

set.seed(1234) 
x <- sample(c('A','B','C','D'), size = 1000, replace= TRUE, prob = c(0.2,0.3,0.3,0.2)) 
y <- rnorm(1000)*1000 
df = data.frame(x= x, y = y) 
ggplot(data = df, mapping = aes(x = x)) + geom_bar(stat = 'count')


######

set.seed(1234) 
x <- sample(c(1,2,4,6,7), size = 1000, replace = TRUE,prob = c(0.1,0.2,0.2,0.3,0.2)) 

ggplot(data = data.frame(x = x), mapping= aes(x = x, y = ..count..)) + geom_bar(stat = 'count')

#####    因子化之后
ggplot(data = data.frame(x = x), mapping = aes(x = factor(x), y = ..count..))+ geom_bar(stat = 'count')


#########

ggplot(data = data.frame(x = x), mapping = aes(x = factor(x), y = ..count..))+ geom_bar(stat = 'count', fill = 'steelblue', colour = 'darkred')



#########   绘制簇条形图
x <- rep(1:5, each = 3)   #each 单个重复3次
y <- rep(c('A','B','C'),times = 5)  #times 整体重复5次
set.seed(1234)    #用1234这个种子来记录后边的随机数
z <- round(runif(min = 10, max = 20, n = 15)) #round取整数，runif
df <- data.frame(x= x, y = y, z = z)
#
ggplot(data = df, mapping = aes(x = factor(x), y = z,fill = y)) + geom_bar(stat = 'identity', position = 'dodge')
#默认堆叠式(stack)
ggplot(data = df, mapping = aes(x = factor(x), y = z, fill = y)) + geom_bar(stat= 'identity')
ggplot(data = df, mapping = aes(x = factor(x), y = z, fill = y)) + geom_bar(stat= 'identity', position = 'stack')
#
ggplot(data = df, mapping = aes(x = factor(x), y = z, fill = y)) + geom_bar(stat= 'identity', position = 'stack') + guides(fill = guide_legend(reverse= TRUE))
#百分比堆叠式
ggplot(data = df, mapping = aes(x = factor(x), y = z, fill = y)) + geom_bar(stat= 'identity', position = 'fill')

#配色
ggplot(data = df, mapping = aes(x = factor(x), y = z, fill = y)) + geom_bar(stat= 'identity', position = 'dodge') + scale_fill_brewer(palette = 'Accent')
#自定义配色
col <- c('darkred','skyblue','purple')
ggplot(data = df, mapping =aes(x = factor(x), y = z, fill = y)) + geom_bar(stat = 'identity', colour= 'black', position = 'dodge') + scale_fill_manual(values = col, limits= c('B','C','A')) + xlab('x')

#######
a <- ggplot(mpg, aes(x=hwy))
a + stat_bin(aes(fill=..count.., color=-1*..ndensity..), binwidth = 1)

####
x <- c('A','B','C','D','E','F','G')
y <-c('xx','yy','yy','xx','xx','xx','yy')
z <- c(10,33,12,9,16,23,11) 
df<- data.frame(x = x, y = y, z = z)
ggplot(data = df, mapping = aes(x= x, y = z, fill = y)) + geom_bar(stat = 'identity')

#####
ggplot(data = df, mapping = aes(x = reorder(x, z), y = z, fill = y)) +geom_bar(stat = 'identity') + xlab('x')

#------------------------------------------------------------------------------------------------------------------
#####
set.seed(12)
x <- 1980 + 1:35
y <- round(100*rnorm(35))#rnorm生成符合正态分布的随机数
df <- data.frame(x = x,y = y)
# 判断y是否为正值
df <- transform(df,judge = ifelse(y>0,"YES","NO")) #构建第新的一列，判定y的正负

# 去除图例用theme()主题函数
p=ggplot(df,aes(x = x,y = y,fill = judge))+geom_bar(stat = "identity")
p=p+theme(legend.position= "")   #去掉图例
p=p+xlab("Year")
p=p+scale_fill_manual(values = c("darkred","blue"))

# 去除图例用guide=FALSE
p=ggplot(data = df, mapping = aes(x = x, y = y, fill = judge))+ geom_bar(stat = 'identity', position = 'identity')
p=p+xlab('Year') 
p=p+scale_fill_manual(values = c('blue','red'), guide = FALSE)   #也可以通过guide=FALSE去除图例
p
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#组间距离
x <- c("A","B","C","D","E")
y <- c(10,20,15,22,18)
df <- data.frame(x = x,y = y)
# 不作任何条形宽度的调整(默认为0.9)
p=ggplot(df,aes(x = x,y = y))
p=p+geom_bar(stat = "identity",fill = "steelblue",colour = "black") 
# 调整条形宽度为1
ggplot(df,aes(x = x,y = y))+geom_bar(stat = "identity",fill = "steelblue",colour = "black",width = 1)

















#----------------------------------------------------------------------------------------------
#组内距离
x <- rep(1:5,each = 3)
y <- rep(c("A","B","C"),times = 5)
set.seed(12)
z <- round(runif(min = 10,max = 20,n = 15))
df <- data.frame(x = x,y = y,z = z)


# 不做任何条形宽度和条形距离的调整
#条形宽度默认为0.9，组间距离默认为0.1，组内距离默认为0
ggplot(data = df, mapping = aes(x = factor(x), y = z, fill = y))+geom_bar(stat = "identity",position = "dodge",width=1)
# 这个设置就是条形宽度为0.5，dodge宽度为0.7，由于有一个坐标轴对对应3条柱子，所有组内距离为0.1
ggplot(data = df, mapping = aes(x = factor(x), y = z, fill = y))+geom_bar(stat= 'identity', width = 0.5, position = position_dodge(0.7))


#精确测定组内和组间距离
p=ggplot(data = df, mapping = aes(x = x, y = z, fill = y))+geom_bar(stat= 'identity', width = 0.3, position = position_dodge(1.35))
p=p+scale_x_continuous(breaks=seq(0,5.5,0.1))
p=p+theme(axis.text.x=element_text(angle=45,colour="black",size=8,hjust=1))
p
#------------------------------------------------------------------------------------------------
#添加数据标签

p=ggplot(df,aes(x = interaction(x,y),y = z,fill = y))+geom_bar(stat = "identity") #interaction合并x和y列作为一因子，并用.间隔
p=p+geom_text(aes(label = z))   #aes映射标签，默认字体4号？，颜色为黑色，位置为0.5(在bar边界的中间)


p=ggplot(data = df, mapping = aes(x = interaction(x,y), y = z, fill = y))+ geom_bar(stat = 'identity')  
p=p+ylim(0,max(z)+1) 
p=p+geom_text(mapping =aes(label = z), size = 4, colour = 'orange', vjust = -0.5)#调整标签的大小，颜色，位置(正数往下走，负数往上走)

#vjust调整标签位置，1为分界线，越大于1，标签越在条形图上界下方，反之则越在条形图上上界上方
# vjust 调整标签竖直位置,越大,标签越在条形图的上界下方；0.5时，则在中间。
# hjust 调整标签水平位置，越大,标签越在条形图的上界左边；0.5时，则在中间。


 #bar的默认位置是identity,text的默认位置也是identity,如果bar位置变成了其他的形式，text的位置也要变成对应的

###dodge
ggplot(data = df, mapping = aes(x = x, y = z, fill = y)) + geom_bar(stat= 'identity', position = 'dodge') + 
  geom_text(mapping = aes(label = z),size = 5, colour = 'black', vjust = 1, hjust = 0.5, position = position_dodge(0.9))

#stack
ggplot(data = df, mapping = aes(x = x, y = z, fill = y)) + geom_bar(stat= 'identity', position = 'stack') + 
  geom_text(mapping = aes(label = z),size = 5, colour = 'black', vjust = 3.5, hjust = .5, position = position_stack())




 #-----------------------------------------------------------------------------------------------------------------------------
#补充:统计变换 
#若x轴变量为连续的，则用sta = bin； 
#若离散型的,可用stat = “count”或stat = “identity”





#--------------------------------------------------------------------------------------------------------------------
  
  
  
  
  

