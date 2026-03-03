<?php
namespace IPP\Student;

use IPP\Student\InterpreterException;

class SolBlock {
    /**
        *@var array<int, string> $parameters
    */
    public array $parameters = []; // block parameters
    /**
        *@var array<int, SolStatement> $statements
    */
    public array $statements = []; // block statements
    public int $arity; // # of parameters

    public SolVariable $self; // self variable

    /**
     * @param array<int, SolVariable> $blockcallparameters
     */
    public function evaluate(array $blockcallparameters, Interpreter $interpreter): SolVariable {
        $callvariables = [];
        $callvariables["self"] = $this->self; // add self to variables
        $totalparameters = count($this->parameters);
        $totalcallparameters = count($blockcallparameters);
        if($totalcallparameters != $totalparameters){
            // wrong number of parameters when calling
            throw new InterpreterException("Wrong block arguments", 51);
        }
        $blockcallparameters = array_values($blockcallparameters);
        for($i = 1; $i < $totalparameters+1; $i++){
            // add parameters into variables
            $callvariables[$this->parameters[(int) $i]] = $blockcallparameters[$i-1];
        }

        $lastevaluatedstatement = new SolVariable("_", "Nil", "nil");

        foreach($this->statements as $statement){
            // evaluate statements
            $lastevaluatedstatement = $statement->execute($callvariables, $interpreter);
        }
        return $lastevaluatedstatement; // return last evaluated statement
    }

    public function __construct(\DOMElement $block){
        $this->arity = (int) $block->getAttribute("arity");
        $parelements = $block->getElementsByTagName("parameter");
        foreach($parelements as $parelement){
            $parorder = $parelement->getAttribute("order");
            $parname = $parelement->getAttribute("name");
            $this->parameters[$parorder] = $parname;
        }

        $statelements = $block->getElementsByTagName("assign");
        foreach($statelements as $statelement){
            $statorder = $statelement->getAttribute("order");
            $this->statements[$statorder] = new SolStatement($statelement);
        }
    }
}