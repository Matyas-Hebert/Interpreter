<?php
namespace IPP\Student;

class SolVariable {
    public string $name; // variable name
    public string $type; // class or name of class
    public string $value; // value of the variable
    public ?SolBlock $block; // block saved in a variable might be null

    /**
        *@var array<string, SolVariable> $attributes
    */
    public array $attributes = []; // an array of variables

    public function __construct(string $name, string $type, string $value, ?SolBlock $block = null){
        // constructor
        $this->name = $name;
        $this->type = $type;
        $this->value = $value;
        $this->block = $block;
    }
}