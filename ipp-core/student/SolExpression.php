<?php
namespace IPP\Student;

use IPP\Student\InterpreterException;

class SolExpression {
    public int $type = -1; // type where: 0 - literal, 1 - var, 2 - block, 3 - send
    public ?SolLiteral $literal = null;
    public ?string $var = null;
    public ?SolBlock $block = null;
    public ?SolSend $send = null;

    /**
     * @param array<string, SolVariable> $variables
     */
    public function evaluate(array &$variables, Interpreter $interpreter): SolVariable {
        if ($this->type == 0) {
            $variable = new SolVariable("a", $this->literal->class, $this->literal->value);
            // returns the evaluated literal
            return $variable;
        }
        else if ($this->type == 1) {
            if(!array_key_exists($this->var, $variables)){
                // variables doesnt exists throwing an exception
                throw new InterpreterException("Wrong variable", 52);
            }
            return $variables[$this->var];
        }
        else if ($this->type == 2) {
            $variable = new SolVariable("_", "Block", "block", $this->block);
            $variable->block->self = $variables["self"]; // setting a self variable of the block at the point of creation
            return $variable;
        }
        else if ($this->type == 3) {
            $methodtocall = $this->send->selector;
            $sender = $this->send->expression->evaluate($variables, $interpreter);
            $arguments = $this->send->arguments;
            $classtocall = $sender->type;

            $parameters = [];
            $parcount = count($arguments);
            for($i = 1; $i <= $parcount; $i++){
                $evaluation = $arguments[$i]->evaluate($variables, $interpreter); // evaluating arguments
                $parameters[$i] = $evaluation;
            }

            if($methodtocall == "from:"){
                $selfclass = $sender->value;
                $arg1 = clone $parameters[1];
                $argclass = $arg1->type;
                // check whether $selfclass is ancestor of $argclass if usage from: is valid
                while($selfclass != $argclass){
                    if(!array_key_exists($selfclass, $interpreter->classes)){
                        throw new InterpreterException("Wrong from", 53);
                    }
                    $selfclass = $interpreter->classes[$selfclass]->parent;
                }
                $class = $sender->value;
                $arg1->type = $class;
                return $arg1; // returning the result of from
            }

            if($classtocall == "class"){
                $classtocall = $sender->value;
            }

            if($interpreter->isbuildinclass($classtocall)){
                return $interpreter->callbuildinmethod($classtocall, $methodtocall, $sender, $parameters); // calling of build-in method
            }
            $class = $interpreter->classes[$classtocall];
            // find which build - in does the class extends or in which class is the called method in
            while(!$class->containMethod($methodtocall)){
                $classtocall = $class->parent;
                if($interpreter->isbuildinclass($classtocall)){
                    return $interpreter->callbuildinmethod($classtocall, $methodtocall, $sender, $parameters);
                }
                $class = $interpreter->classes[$classtocall];
            }
            $result = $class->methods[$methodtocall]->call($sender, $parameters, $interpreter); // call the method
            return $result;
        }
        return new SolVariable("_", "Nil", "nil");
    }

    public function __construct(\DOMElement $expression) {

        $children = $expression->childNodes;

        foreach ($children as $child) {
            if (!($child instanceof \DOMElement)) {
                continue;
            }
            switch($child->nodeName){
                case 'literal':
                    $literalelement = $child;
                    $this->type = 0;
                    $literalvalue = $literalelement->getAttribute("value");
                    $literalclass = $literalelement->getAttribute("class");
                    $this->literal = new SolLiteral($literalvalue, $literalclass);
                    break;
                case 'var':
                    $varelement = $child;
                    $this->type = 1;
                    $this->var = $varelement->getAttribute("name");
                    break;
                case 'block':
                    $blockelement = $child;
                    $this->type = 2;
                    $this->block = new SolBlock($blockelement);
                    break;
                case 'send':
                    $sendelement = $child;
                    $this->type = 3;
                    $this->send = new SolSend($sendelement);
                    break;
            }
        }
        return;
    }
}