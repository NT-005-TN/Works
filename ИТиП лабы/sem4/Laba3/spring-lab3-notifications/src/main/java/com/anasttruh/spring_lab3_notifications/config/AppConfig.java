package com.anasttruh.spring_lab3_notifications.config;

import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan("org.example")
public class AppConfig {
    // Бины создаются автоматически благодаря сканированию компонентов
}

/*
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 3 (Java Config): Явное создание бинов через @Bean
// -------------------------------------------------------------------------
// @Configuration
// public class AppConfig {
//
//     @Bean
//     public EmailService emailService() {
//         return new EmailService();
//     }
//
//     @Bean
//     public SmsService smsService() {
//         return new SmsService();
//     }
//
//     @Bean
//     public NotificationManager notificationManager() {
//         return new NotificationManager(emailService());
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. Высокая трудоемкость: при добавлении каждого нового сервиса нужно вручную
//    писать метод @Bean в этом классе.
// 2. Нарушение принципа Open/Closed: класс конфигурации постоянно меняется.
// 3. Автоматическое сканирование (@ComponentScan) удобнее для большинства случаев,
//    так как аннотации @Service находятся прямо в классах сервисов.
// 4. При переходе на аннотации явная конфигурация становится избыточной.
*/