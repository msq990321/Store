# '调整工作目录'
wd <- "C:/Users/Administrator/Desktop/R"
setwd(wd)
cat('当前工作目录：',getwd(),sep = '')

# '加载包和加载数据'
library(readxl)
library(ggplot2)
library(ggpp)
library(ggpmisc)
df <- read_excel("datasets/data.xlsx")
# View(df)
# data1 <- subset(df,'tiaojian')

flm <- y~0+x
# 画图
ggplot(df,aes(x,y))+
  geom_point(aes(color='Phylum'))+
  
  geom_smooth(method = 'lm',se = F,formula = flm,color = 'grey')+
  
  stat_poly_eq(formula = flm,
               coef.digits = 5,
               rr.digits = 5,
               aes(label = paste(..eq.label..,..rr.label..,sep = '~~~')),
               parse = T)+
  labs(title = bquote('fitting Function about test'))+theme(plot.title = element_text(hjust = 0.5))

# 保存为tiff
ggsave('pics/fitting.tiff',dpi = 450,)
dev.off()