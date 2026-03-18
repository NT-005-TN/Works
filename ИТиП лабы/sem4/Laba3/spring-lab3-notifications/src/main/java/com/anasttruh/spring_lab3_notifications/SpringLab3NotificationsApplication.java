package com.anasttruh.spring_lab3_notifications;

import com.anasttruh.spring_lab3_notifications.config.AppConfig;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Import;

@SpringBootApplication
@Import(AppConfig.class)
public class SpringLab3NotificationsApplication {
	public static void main(String[] args) {
		SpringApplication.run(SpringLab3NotificationsApplication.class, args);
	}
}

/*
// -------------------------------------------------------------------------
// ВАРИАНТ ЧАСТИ 0/1: Без явного импорта конфигурации
// -------------------------------------------------------------------------
// @SpringBootApplication
// public class Application {
//     public static void main(String[] args) {
//         SpringApplication.run(Application.class, args);
//     }
// }
//
// ПОЧЕМУ ОТКАЗАЛИСЬ ОТ ЭТОГО ВАРИАНТА:
// 1. В Части 3 мы использовали отдельный класс AppConfig для Java Config.
// 2. Чтобы Spring увидел этот класс и применил настройки (например, @ComponentScan),
//    нужно явно импортировать его через @Import, так как AppConfig не находится
//    в том же пакете, что и основной класс Application.
// 3. Явный импорт делает конфигурацию более предсказуемой и понятной.
*/