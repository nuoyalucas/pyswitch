# pyswitch
<h1>五行代码在python中实现switch ！！！</h1>
这个函数接收两个参数:<br/>
<code>
switch(variable,case)
</code><br/>
variable指的是需要判断的值；case是一个字典<br/>
具体用法如下:
<pre>
<code>
case={
  'a':'print("a")',
  'b':'print("b")',
  'c':'print("c")'
}
switch('b',case)
输出:b
</code>
</pre>
其中，case的key表示variabl是否等于这个值，如果是，执行对应的value的代码，否则，跳到下一个key进行判断。<br />
<h3>注意：value内需要执行的代码要用引号包裹起来，否则没有效果</h3>
