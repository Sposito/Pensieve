# RTC Wake system from S5 Real Time Clock Wake

Funcionalidade da [[bios|BIOS]] que permite programar o sistema para ligar automaticamente a partir do estado S5 (completamente desligado, mas conectado à energia) em uma data e hora específicas, usando o relógio de tempo real (RTC) da placa-mãe.

## Status e Uso

Estado da configuração na [[huananzhi-x99-f8d-plus]].

- Status: `[Disabled]`
- Uso Típico: Agendar tarefas automáticas que requerem que o PC ligue sozinho (ex: backups noturnos, início de downloads).
- Relação com outros estados: Não afeta a capacidade de acordar de [[acpi_sleep_states#S3 Suspend to RAM|S3]] (suspensão) ou [[acpi_sleep_states#S4 Hibernate to Disk|S4]] (hibernação) via teclado, mouse ou [[Wake-on-LAN|Wake on Lan]]. O RTC Wake é exclusivamente para ligar a partir do estado S5.