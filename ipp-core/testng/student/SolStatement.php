<?php
namespace IPP\Student;

class SolStatement {
    public string $var = "empty"; // variable to save result of the expression to
    public SolExpression $expression; // expression to be evaluated

    /**
     * @param array<string, SolVariable> $variables
     */
    public function execute(array &$variables, Interpreter $interpreter): ?SolVariable{
        $var = $this->expression->evaluate($variables, $interpreter); // evaluates the expression
        $var->name = $this->var;
        $variables[$var->name] = $var;
        return $var; // returns the result
    }
    public function __construct(\DOMElement $statelement)
    {
        $varelements = $statelement->getElementsByTagName("var");
        foreach ($varelements as $var) {
            $this->var = $var->getAttribute("name");
            break;
        }
        $exprelements = $statelement->getElementsByTagName("expr");
        foreach ($exprelements as $expr){
            $this->expression = new SolExpression($expr);
            break;
        }
    }
}