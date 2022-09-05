library(ggplot2)
library(ggpp)
library(ggpmisc)

# 设置工作目录为R
rm(list = ls())
setwd(dir = 'C:/Users/Administrator/Desktop/自己写的一些程序/R/线性拟合')
cat('当前工作目录：',getwd(),sep = '')
first_file_name <- list.files("datasets")
# 读取数据集文件及以及子文件夹
dir <- paste('./datasets/',first_file_name,sep = '')#新建目录
n <- length(dir)
# print(list.files(dir))

n_sub <- rep(0,n)#生成n个零向量,此处n等于文件夹数目
n_sub <- as.data.frame(n_sub)#转换成数据框
n_sub <- t(n_sub)#转置数据框

for (i in 1:n){
  b = list.files(dir[i])#读取各个文件夹里面的表格数据，b是表格名
  print(b)
  n_sub[i] = length(b)#第一个文件夹中文件数目
  for (j in 1:n_sub[i]){
    file = paste(dir[i],'/',b[j],sep = '')
    df <- readxl::read_excel(file)
    #当前文件名
    bname <- strsplit(b[j],'\\.')[[1]][1]
    tname <- paste(bname,'.tiff',sep = '')
    
    flm <- y~0+x
    
    # 画图，线性拟合绘图
    ggplot(df,aes(x,y))+
      geom_point(aes(color='Phylum'))+
      
      geom_smooth(method = 'lm',se = F,formula = flm,color = 'grey')+
      
      stat_poly_eq(formula = flm,
                   coef.digits = 5,
                   rr.digits = 5,
                   aes(label = paste(..eq.label..,..rr.label..,sep = '~~~')),
                   parse = T)+
      labs(title = bname)+theme(plot.title = element_text(hjust = 0.5))
    
    # 保存为tiff
    ggsave(file = tname,dpi = 450,)
    dev.off()
  }
}