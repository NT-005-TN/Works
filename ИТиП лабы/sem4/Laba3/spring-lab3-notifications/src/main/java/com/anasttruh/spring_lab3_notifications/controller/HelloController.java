package com.anasttruh.spring_lab3_notifications.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/hello")
    public String sayHello() {
        return "Привет, Spring Boot!";
    }

    @GetMapping("/goodbye")
    public String sayGoodbye() {
        return "До свидания, Spring Boot!";
    }

    @GetMapping("/greet")
    public String greet(@RequestParam String name) {
        return "Привет, " + name + "!";
    }

    @GetMapping("/user")
    public String userInfo(@RequestParam String name, @RequestParam int age) {
        return "Пользователь: " + name + ", Возраст: " + age;
    }
}

/*
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 1: Базовый контроллер
// -------------------------------------------------------------------------
// @RestController
// public class HelloController {
//
//     @GetMapping("/hello")
//     public String sayHello() {
//         return "Привет, Spring Boot!";
//     }
// }
//
// ПОЧЕМУ ИЗМЕНИЛИ ЭТОТ ВАРИАНТ:
// 1. Добавлены методы для самостоятельного задания (goodbye, greet, user).
// 2. Это демонстрирует работу с @RequestParam и обработку разных путей.
// 3. Расширенный функционал показывает более полное понимание работы REST-контроллеров.
*/