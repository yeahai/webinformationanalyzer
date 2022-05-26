# webinformationanalyzer

## 注意,这只用于学习,其他的与我无关,与我用到的别人中的代码的人也无关. 参考学习

### 这只是一个二创小项目.

通过使用webanalyzer插件的api来进行网站分析,我找到了很多对一个网站分析的工具,但是没有批量对网站进行分析且分类.
于是,我在别人项目的基础之上修改了一些内容,然后通过自己写的文件来进行以下功能:
1. 对网站的子域名进行收集,通过SSL证书和子域名爆破来进行收集(注: 子域名爆破方法哪里使用了超时注解,因为字典很大,设置了3分钟时间,超时则停止)
2. 对于收集的子域名进行去重,去掉重复子域名.
3. 对收集的子域名进行webanalyzer分析,对于分析结构保存为字典格式
4. 对字典格式进行json转换,方便数据传输.
5. 对分析后的结果进行web架构分类.

