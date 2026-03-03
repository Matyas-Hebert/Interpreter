<?php
namespace IPP\Student;

use IPP\Core\AbstractInterpreter;
use IPP\Core\ReturnCode;
use IPP\Core\FileInputReader;
use IPP\Core\Exception\NotImplementedException;
use IPP\Student\InterpreterException;

class Interpreter extends AbstractInterpreter
{
    // array of classes
    /**
        *@var array<string, SolClass>
    */
    public array $classes = [];

    // array of builtin classes
    /**
     * @var array<int, string>
     */
    public array $builtinclasses = ["Object", "Nil", "True", "False", "Integer", "String", "Block"];

    /**
     * Checks whether class is a built-in class
     *
     * @param string $class Name of a class.
     * @return bool Is it a built-in class?
     */
    public function isbuildinclass(string $class): bool{
        return in_array($class, $this->builtinclasses);
    }

    /**
     * Checks whether class is a child class of parent
     *
     * @param string $class Name of a class.
     * @param string $parent Name of a parent class.
     * @return bool Is parent a parent class of class?
     */
    public function checkifparentexists(string $class, string $parent): bool{
        while($class != $parent){
            if(!array_key_exists($class, $this->classes)){
                return false;
            }
            $class = $this->classes[$class]->parent;
        }
        return true;
    }

    /**
     * Adds an attribute to an object, updating its value.
     *
     * @param string $attrname The name of the attribute
     * @param SolVariable &$callvariables Add the attribute here
     * @param SolVariable $attrvalue attribute value.
     * 
     * @return void This function does not return anything.
     */
    public function addAttribute(string $attrname, SolVariable &$callvariables, SolVariable $attrvalue): void{
        $attrname = substr($attrname, 0, -1);
        $callvariables->attributes[$attrname] = $attrvalue;
    }

    /**
     * Updates the attributes of a variable or retrieve an attribute
     *
     * @param array<int, SolVariable> $arguments Arguments of the message
     * @param string                  $method    Name of the attribute
     * @param SolVariable             &$sender   Sender of the message
     *
     * @return SolVariable The new or existing attribute value.
     */
    public function handleAttributes(array $arguments, string $method, SolVariable &$sender):SolVariable{
        $argamount = count($arguments);
        if($argamount == 1){
            $attrname = substr($method, 0, -1);
            $sender->attributes[$attrname] = $arguments[1];
            $evaluated = $arguments[1];
            return $evaluated;
        }
        else if($argamount > 1){
            throw new InterpreterException("Wrong message", 51);
        }
        else{
            if(!array_key_exists($method, $sender->attributes)){
                throw new InterpreterException("Attribute doesnt exists", 51);
            }
            return $sender->attributes[$method];
        }
    }

    /**
     * calls a build-in method
     * 
     * @param string                    $class name of a class
     * @param string                    $method name of a method called
     * @param SolVariable               $sender sender of the message in this case self
     * @param array<int, SolVariable>   $arguments arguments of the message
     */
    public function callbuildinmethod(string $class, string $method, SolVariable $sender, array $arguments): SolVariable{
        $callvariables = []; // each call have its own set of variables
        $callvariables["self"] = clone $sender; // adding self to variables
        // definition of each build-in method
        switch ($class){
            case "Object":
                switch ($method){
                    case "identicalTo:":
                        $arg1 = $arguments[1]; // get first attribute
                        $selfattribute = $callvariables["self"];
                        if($arg1->value == $selfattribute->value && $arg1->type == $selfattribute->type){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "equalTo:":
                        $arg1 = $arguments[1];
                        $arg1value = $arg1->value;
                        if($arg1value == $callvariables["self"]->value){
                            return new SolVariable("_", "True", "true");
                        }
                        else{
                            return new SolVariable("_", "False", "false");
                        }
                    case "asString":
                        return new SolVariable('_', "String", '');
                    case "isNumber":
                        return new SolVariable("_", "False", "false");
                    case "isString":
                        return new SolVariable("_", "False", "false");
                    case "isBlock":
                        return new SolVariable("_", "False", "false");
                    case "isNil":
                        return new SolVariable("_", "False", "false");
                    case "new":
                        return new SolVariable("_", "Object", "");
                    default:
                        // adding or getting an attribute
                        return $this->handleAttributes($arguments, $method, $sender);
                }
            case "Nil":
                switch ($method){
                    case "identicalTo:":
                        $arg1 = $arguments[1];
                        $selfattribute = $callvariables["self"];
                        if($arg1->value == $selfattribute->value && $arg1->type == $selfattribute->type){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "equalTo:":
                        $arg1 = $arguments[1];
                        $arg1value = $arg1->value;
                        // is the Nil equal to the argument
                        if($arg1value == $callvariables["self"]->value){
                            return new SolVariable("_", "True", "true");
                        }
                        else{
                            return new SolVariable("_", "False", "false");
                        }
                    case "asString":
                        return new SolVariable('_', "String", "nil");
                    case "isNumber":
                        return new SolVariable("_", "False", "false");
                    case "isString":
                        return new SolVariable("_", "False", "false");
                    case "isBlock":
                        return new SolVariable("_", "False", "false");
                    case "isNil":
                        return new SolVariable("_", "True", "true");
                    case "new":
                        return new SolVariable("_", "Nil", "nil");
                    default:
                        return $this->handleAttributes($arguments, $method, $sender);
                }
            case "True":
                switch ($method){
                    case "identicalTo:":
                        $arg1 = $arguments[1];
                        $selfattribute = $callvariables["self"];
                        if($arg1->value == $selfattribute->value && $arg1->type == $selfattribute->type){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "equalTo:":
                        $arg1 = $arguments[1];
                        $arg1value = $arg1->value;
                        if($arg1value == $callvariables["self"]->value){
                            return new SolVariable("_", "True", "true");
                        }
                        else{
                            return new SolVariable("_", "False", "false");
                        }
                    case "asString":
                        return new SolVariable("_", "String", "true");
                    case "not":
                        return new SolVariable("_", "False", "false");
                    case "and:":
                        $arg1 = $arguments[1];
                        if($arg1->type == "Block"){
                            // evaluating block variable
                            $arg1 = $arguments[1]->block->evaluate([], $this);
                        }
                        else{
                            $arg1 = $arguments[1]->attributes["value"];
                        }
                        return $arg1;
                    case "or:":
                        return new SolVariable("_", "True", "true");
                    case "ifTrue:ifFalse:":
                        $arg1 = $arguments[1];
                        return $arg1->block->evaluate([], $this);
                    case "isNumber":
                        return new SolVariable("_", "False", "false");
                    case "isString":
                        return new SolVariable("_", "False", "false");
                    case "isBlock":
                        return new SolVariable("_", "False", "false");
                    case "isNil":
                        return new SolVariable("_", "False", "false");
                    case "new":
                        return new SolVariable("_", "True", "true");
                    default:
                        return $this->handleAttributes($arguments, $method, $sender);
                }
            case "False":
                switch ($method){
                    case "identicalTo:":
                        $arg1 = $arguments[1];
                        $selfattribute = $callvariables["self"];
                        if($arg1->value == $selfattribute->value && $arg1->type == $selfattribute->type){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "equalTo:":
                        $arg1 = $arguments[1];
                        $arg1value = $arg1->value;
                        if($arg1value == $callvariables["self"]->value){
                            return new SolVariable("_", "True", "true");
                        }
                        else{
                            return new SolVariable("_", "False", "false");
                        }
                    case "asString":
                        return new SolVariable("_", "String", "false");
                    case "not":
                        return new SolVariable("_", "True", "true");
                    case "and:":
                        return new SolVariable("_", "False", "false");
                    case "or:":
                        $arg1 = $arguments[1];
                        if($arg1->type == "Block"){
                            $arg1 = $arguments[1]->block->evaluate([], $this);
                        }
                        else{
                            $arg1 = $arguments[1]->attributes["value"];
                        }
                        return $arg1;
                    case "ifTrue:ifFalse:":
                        $arg2 = $arguments[2];
                        // evaluating second argument because sender is False
                        return $arg2->block->evaluate([], $this);
                    case "isNumber":
                        return new SolVariable("_", "False", "false");
                    case "isString":
                        return new SolVariable("_", "False", "false");
                    case "isBlock":
                        return new SolVariable("_", "False", "false");
                    case "isNil":
                        return new SolVariable("_", "False", "false");
                    case "new":
                        return new SolVariable("_", "False", "false");
                    default:
                        return $this->handleAttributes($arguments, $method, $sender);
                }
            case "Integer":
                switch ($method){
                    case "identicalTo:":
                        $arg1 = $arguments[1];
                        $selfattribute = $callvariables["self"];
                        if($arg1->value == $selfattribute->value && $arg1->type == $selfattribute->type){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "equalTo:":
                        $arg1 = $arguments[1];
                        $arg1value = $arg1->value;
                        if($arg1value == $callvariables["self"]->value){
                            return new SolVariable("_", "True", "true");
                        }
                        else{
                            return new SolVariable("_", "False", "false");
                        }
                    case "asString":
                        $newvar = $callvariables["self"];
                        $newvar->type = "String";
                        return $newvar;
                    case "greaterThan:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Integer")){
                            throw new InterpreterException("Wrong attribute type", 53);
                        }
                        $selfvalue = (int) $callvariables["self"]->value;
                        $arg1value = (int) ($arg1->value);
                        if($selfvalue > $arg1value){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "plus:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Integer")){
                            throw new InterpreterException("Wrong attribute type", 53);
                        }
                        $arg1value = (int) $arg1->value;
                        $result = $callvariables["self"];
                        // add the values
                        $result->value = (string) ((int) $callvariables["self"]->value + $arg1value);
                        return $result;
                    case "minus:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Integer")){
                            throw new InterpreterException("Wrong attribute type", 53);
                        }
                        $arg1value = (int) $arg1->value;
                        $result = $callvariables["self"];
                        // subtract the values
                        $result->value = (string) ((int) $callvariables["self"]->value - $arg1value);
                        return $result;
                    case "multiplyBy:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Integer")){
                            throw new InterpreterException("Wrong attribute type", 53);
                        }
                        $arg1value = (int) $arg1->value;
                        $result = $callvariables["self"];
                        $a = $callvariables["self"];
                        $result->value = (string) ((int) $callvariables["self"]->value * $arg1value);
                        return $result;
                    case "divBy:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Integer")){
                            throw new InterpreterException("Wrong attribute type", 53);
                        }
                        $arg1value = (int) $arg1->value;
                        if($arg1value == 0){
                            // cant divide by 0
                            throw new InterpreterException("Wrong attribute type", 53);
                        }
                        $result = $callvariables["self"];
                        $result->value = (string) (intdiv((int) $callvariables["self"]->value, $arg1value));
                        return $result;
                    case "asInteger":
                        $result = $callvariables["self"];
                        return $result;
                    case "timesRepeat:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Block")){
                            throw new InterpreterException("Wrong attribute type", 53);
                        }
                        $selfvalue = (int) $callvariables["self"]->value;
                        $result = new SolVariable("_", "Nil", "nil");
                        if($selfvalue > 0){
                            // repeat evaluating of the block n times
                            for($i = 1; $i <= $selfvalue; $i++){
                                $arg = new SolVariable("_", "Integer", "$i");
                                $pars = [];
                                $pars[1] = $arg;
                                $result = $arg1->block->evaluate($pars, $this);
                            }
                        }
                        return $result;
                    case "isNumber":
                        return new SolVariable("_", "True", "true");
                    case "isString":
                        return new SolVariable("_", "False", "false");
                    case "isBlock":
                        return new SolVariable("_", "False", "false");
                    case "isNil":
                        return new SolVariable("_", "False", "false");
                    case "new":
                        return new SolVariable("_", "Integer", "");
                    default:
                        return $this->handleAttributes($arguments, $method, $sender);
                }
            case "String":
                switch ($method){
                    case "identicalTo:":
                        $arg1 = $arguments[1];
                        $selfattribute = $callvariables["self"];
                        if($arg1->value == $selfattribute->value && $arg1->type == $selfattribute->type){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "equalTo:":
                        $arg1 = $arguments[1];
                        $arg1value = $arg1->value;
                        if($arg1value == $callvariables["self"]->value){
                            return new SolVariable("_", "True", "true");
                        }
                        else{
                            return new SolVariable("_", "False", "false");
                        }
                    case "asString":
                        return $callvariables["self"];
                    case "read":
                        $val = $this->input->readString();
                        return new SolVariable("_", "String", $val);
                    case "print":
                        $this->stdout->writeString($callvariables["self"]->value);
                        return $callvariables["self"];
                    case "asInteger":
                        $result = $callvariables["self"];
                        if(is_numeric($callvariables["self"]->value)){
                            $result->type = "Integer";
                            return $result;
                        }
                        return new SolVariable("_", "Nil", "nil");
                    case "concatenateWith:":
                        $arg1 = $arguments[1];
                        $class = $arg1->type;
                        $concat = $this->checkifparentexists($class, "String");
                        if($concat == false){
                            return new SolVariable("_", "Nil", "nil");
                        }
                        // use . operator to do the concatenation
                        $value = $callvariables["self"]->value . $arg1->value;
                        return new SolVariable("_", "String", $value);
                    case "startsWith:endsBefore:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Integer")){
                            throw new InterpreterException("Wrong Argument type", 53);
                        }
                        $arg2 = $arguments[2];
                        if(!$this->checkifparentexists($arg2->type, "Integer")){
                            throw new InterpreterException("Wrong Argument type", 53);
                        }
                        $arg1value = (int) $arg1->value;
                        $arg2value = (int) $arg2->value;
                        $selfvalue = $callvariables["self"]->value;
                        $strlen = strlen($selfvalue);
                        if($arg1value >= $strlen){
                            return new SolVariable("_", "String", "");
                        }
                        if($arg2value >= $strlen){
                            $arg2value = $strlen;
                        }
                        if($arg1value <= 0 || $arg2value <= 0){
                            return new SolVariable("_", "Nil", "nil");
                        }
                        if($arg2value-$arg1value <= 0){
                            return new SolVariable("_", "String", "");
                        }
                        $substring = substr($selfvalue, $arg1value-1, $arg2value-$arg1value);
                        return new SolVariable("_", "String", "$substring");
                    case "isNumber":
                        return new SolVariable("_", "False", "false");
                    case "isString":
                        return new SolVariable("_", "True", "true");
                    case "isBlock":
                        return new SolVariable("_", "False", "false");
                    case "isNil":
                        return new SolVariable("_", "False", "false");
                    case "new":
                        return new SolVariable("_", "String", "");
                    default:
                        return $this->handleAttributes($arguments, $method, $sender);
                }
            case "Block":
                switch ($method){
                    case "identicalTo:":
                        $arg1 = $arguments[1];
                        $selfattribute = $callvariables["self"];
                        if($arg1->value == $selfattribute->value && $arg1->type == $selfattribute->type){
                            return new SolVariable("_", "True", "true");
                        }
                        return new SolVariable("_", "False", "false");
                    case "equalTo:":
                        $arg1 = $arguments[1];
                        $arg1value = $arg1->value;
                        if($arg1value == $callvariables["self"]->value){
                            return new SolVariable("_", "True", "true");
                        }
                        else{
                            return new SolVariable("_", "False", "false");
                        }
                    case "asString":
                    case "whileTrue:":
                        $arg1 = $arguments[1];
                        if(!$this->checkifparentexists($arg1->type, "Block")){
                            throw new InterpreterException("Wrong Argument type", 53);
                        }
                        $whilecond = $callvariables["self"]->block->evaluate([], $this);
                        $laststat = new SolVariable("_", "Nil", "nil");
                        // while the value of self is True call the block argument
                        while($whilecond->type == "True"){
                            $laststat = $arg1->block->evaluate([],  $this);
                            $whilecond = $callvariables["self"]->block->evaluate([], $this);
                        }
                        return $laststat;
                    case "isNumber":
                        return new SolVariable("_", "False", "false");
                    case "isString":
                        return new SolVariable("_", "False", "false");
                    case "isBlock":
                        return new SolVariable("_", "True", "true");
                    case "isNil":
                        return new SolVariable("_", "False", "false");
                    case "new":
                        return new SolVariable("_", "Block", "");
                    default:
                        return $callvariables["self"]->block->evaluate($arguments, $this);
                }
            default:
                return $this->handleAttributes($arguments, $method, $sender);
        }
    }

    /**
     * Parse the xml file and process it
     * 
     * @return int
     */
    public function execute(): int
    {
	    ini_set('display_errors', 'stderr');
        $dom = $this->source->getDOMDocument();

        $program = $dom->documentElement;

        $classelements = $program->getElementsByTagName("class");

        foreach ($classelements as $class) {
            $className = $class->getAttribute("name");
            $parentName = $class->getAttribute("parent");

            $newclass = new SolClass($className, $parentName);
            
            $methodelements = $class->getElementsByTagName("method");

            foreach($methodelements as $method) {
                $methodName = $method->getAttribute("selector");
                $newmethod = new SolMethod($methodName);

                $blockelements = $method->getElementsByTagName("block");

                foreach($blockelements as $block) {
                    $blockArity = (int) $block->getAttribute("arity");
                    $newmethod->arity = $blockArity;

                    $parelements = $block->getElementsByTagName("parameter");
                    foreach($parelements as $par) {
                        $order = (int) $par->getAttribute("order");
                        if(!array_key_exists($order, $newmethod->parameters) && $order <= $blockArity){
                            $newmethod->parameters[$order] = $par->getAttribute("name");
                        }
                    }
                    $children = $block->childNodes;
                    foreach($children as $assign){
                        if (!($assign instanceof \DOMElement)) {
                            continue;
                        }
                        $statement = new SolStatement($assign);
                        if($statement->var == "empty"){
                            continue;
                        }
                        $statementorder = $assign->getAttribute("order");
                        if(!array_key_exists($statementorder, $newmethod->statements)){
                            $newmethod->statements[$statementorder] = $statement;
                        }
                    }
                    break;
                }

                $newclass->methods[$methodName] = $newmethod;
            }

            $this->classes[$className] = $newclass;
        }

        if(array_key_exists("Main", $this->classes)){
            if(!array_key_exists("run", $this->classes["Main"]->methods)){
                throw new InterpreterException("Run doesnt exist", 52);
            }
            else{
                $self = new SolVariable("self", "Main", '');
                $this->classes["Main"]->methods["run"]->call($self, [], $this);
            }
        }
        else{
            throw new InterpreterException("Main doesnt exist", 52);
        }
        return 0;
    }
}
