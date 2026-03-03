<?php
namespace IPP\Student;

class SolSend {
    public string $selector; // selector or a name of method
    /**
        *@var array<int, SolExpression>
    */
    public array $arguments = []; // array of arguments
    public SolExpression $expression;

    public function __construct(\DOMElement $sendelement) {
        $this->selector = $sendelement->getAttribute("selector");
        $children = $sendelement->childNodes;
        foreach ($children as $child) {
            if (!($child instanceof \DOMElement)) {
                continue;
            }
            switch($child->nodeName){
                case "arg":
                    $argorder = $child->getAttribute("order");
                    $argchildren = $child->childNodes;
                    foreach ($argchildren as $argchild) {
                        if (!($argchild instanceof \DOMElement)) {
                            continue;
                        }
                        if ($argchild->nodeName == "expr"){
                            $this->arguments[$argorder] = new SolExpression($argchild);
                        }
                    }
                case "expr":
                    $this->expression = new SolExpression($child);
            }
        }
        return;
    }
}