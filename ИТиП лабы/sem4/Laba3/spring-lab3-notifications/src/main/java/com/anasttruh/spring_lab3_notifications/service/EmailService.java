package com.anasttruh.spring_lab3_notifications.service;

import org.springframework.stereotype.Service;

@Service
public class EmailService implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println(" EMAIL to " + recipient + ": " + message);
    }
}

/*
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 2: Обычный Java класс без аннотаций
// -------------------------------------------------------------------------
// public class EmailService implements MessageService {
//     @Override
//     public void sendMessage(String message, String recipient) {
//         System.out.println(" EMAIL to " + recipient + ": " + message);
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. Класс не управляется контейнером Spring (не является бином).
// 2. Нельзя внедрить его через @Autowired в другие классы.
// 3. Приходилось создавать объект вручную через new (жесткая связь).
// 4. Аннотация @Service позволяет Spring автоматически найти и создать бин.
*/