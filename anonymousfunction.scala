// Scala program to illustrate the anonymous method 
object Main 
{ 
    def main(args: Array[String]) 
    { 
        
        // Creating anonymous functions 
        // with multiple parameters Assign 
        // anonymous functions to variables 
        var myfc1 = (str1:String, str2:String) => str1 + str2
        
        // An anonymous function is created 
        // using _ wildcard instead of 
        // variable name because str1 and 
        // str2 variable appear only once 
        var myfc2 = (_:String) + (_:String)

        
        // Here, the variable invoke like a function call 
        println(myfc1("Bigdata", "Scala")) 
        println(myfc2("Bigdata", "forScala")) 
    } 
} 
