<?php
namespace IPP\Student;

class SolMethod {
    public string $name; // name of method
    public int $arity = 0; // amount of arguments
    /**
        *@var array<int, string> $parameters
    */
    public array $parameters = []; // arguments/parameters of a method
    /**
        *@var array<int, SolStatement> $statements
    */
    public array $statements = []; // array of statements
    
    /**
     * @param array<int, SolVariable> $methodcallparameters
     */
    public function call(SolVariable $caller, array $methodcallparameters, Interpreter $interpreter): SolVariable{
        $callvariables = [];
        $callvariables["self"] = clone $caller;
        $totalparameters = count($this->parameters);
        for($i = 1; $i < $totalparameters+1; $i++){
            // go through parameters in correct order
            $callvariables[$this->parameters[(string)$i]] = $methodcallparameters[$i];
        }

        $statcount = count($this->statements);
        $lastevaluatedstatement = new SolVariable("_", "Nil", "nil");
        for($i = 1; $i < $statcount + 1; $i++){
            // evaluate each statement in correct order
            $lastevaluatedstatement = $this->statements[$i]->execute($callvariables, $interpreter);
        }
        return $lastevaluatedstatement;
    }

    public function __construct(string $name){
        $this->name = $name;
    }
}