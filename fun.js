function Foo(name,age) {
    this.Name = name;
    this.Age = age;
    this.Func = function(arg) {
        return this.Name + arg;
    }
}

var obj = new Foo('yuanzy',18);

console.log(obj.Name);
console.log(obj.Age);
var ret = obj.Func('sb');
console.log(ret);
