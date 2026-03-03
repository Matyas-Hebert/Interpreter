<?php
namespace IPP\Student;

class SolClass {
    public string $name; //class name
    public string $parent; // class parent name
    /**
        *@var array<string, SolMethod> $methods
    */
    public array $methods = []; // an array fo methosd

    public function containMethod(string $methodname):?SolMethod{
        // does class contan method $methodname
        if(array_key_exists($methodname, $this->methods)){
            return $this->methods[$methodname];
        }
        else{
            return null;
        }
    }

    public function __construct(string $name, string $parent){
        $this->name = $name;
        $this->parent = $parent;
    }
}