package com.anasttruh.spring_lab3_notifications.service;

import org.springframework.stereotype.Service;

@Service
public class SmsService implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println(" SMS to " + recipient + ": " + message);
    }
}

/*
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 2: Обычный Java класс без аннотаций
// -------------------------------------------------------------------------
// public class SmsService implements MessageService {
//     @Override
//     public void sendMessage(String message, String recipient) {
//         System.out.println(" SMS to " + recipient + ": " + message);
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. Аналогично EmailService: без Spring-аннотаций класс не попадает в контекст.
// 2. Невозможно использовать преимущества DI (внедрения зависимостей).
// 3. Ручное создание объектов нарушает принцип инверсии управления.
*/