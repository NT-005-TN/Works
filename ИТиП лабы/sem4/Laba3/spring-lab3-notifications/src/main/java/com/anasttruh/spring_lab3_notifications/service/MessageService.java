package com.anasttruh.spring_lab3_notifications.service;

public interface MessageService {
    void sendMessage(String message, String recipient);
}

/*
// -------------------------------------------------------------------------
// 1. Интерфейс определяет контракт, который не зависит от реализации Spring.
// 2. Он необходим для полиморфизма и внедрения зависимостей по интерфейсу.
// 3. Позволяет легко добавлять новые реализации без изменения существующего кода.
*/