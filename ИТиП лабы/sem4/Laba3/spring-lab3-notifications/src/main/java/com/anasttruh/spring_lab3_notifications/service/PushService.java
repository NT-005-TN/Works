package com.anasttruh.spring_lab3_notifications.service;

import org.springframework.stereotype.Service;

@Service
public class PushService implements MessageService {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println(" PUSH to " + recipient + ": " + message);
    }
}

/*
// -------------------------------------------------------------------------
// 1. Демонстрирует преимущество внедрения коллекции List<MessageService>.
// 2. При добавлении этого сервиса не нужно менять код NotificationManager,
//    он автоматически подключится к рассылке.
// 3. Показывает масштабируемость подхода с автоматическим сканированием компонентов.
*/