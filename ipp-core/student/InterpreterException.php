<?php

namespace IPP\Student;

use IPP\Core\Exception\IPPException;
use IPP\Core\ReturnCode;

/**
 * Exception thrown by the SOL25 interpreter for runtime errors.
 * Carries a specific return code from IPP\Core\ReturnCode.
 */
class InterpreterException extends IPPException
{
    public function __construct(string $message = "", int $code = ReturnCode::INTERPRET_TYPE_ERROR){
        parent::__construct($message, $code);
    }
}
