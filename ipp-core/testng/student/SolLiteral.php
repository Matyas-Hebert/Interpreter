<?php
namespace IPP\Student;

class SolLiteral {
    public string $value;
    public string $class;  
    public function __construct(string $value, string $class) {
        $this->value = $value;
        $this->class = $class;
    }
}