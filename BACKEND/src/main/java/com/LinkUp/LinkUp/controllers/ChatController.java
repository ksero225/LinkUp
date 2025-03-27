package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.documents.Message;
import com.LinkUp.LinkUp.services.MessageService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;

import java.time.LocalDateTime;

@Controller
public class ChatController {

    private final SimpMessagingTemplate messagingTemplate;
    private final MessageService messageService;

    public ChatController(SimpMessagingTemplate messagingTemplate, MessageService messageService) {
        this.messagingTemplate = messagingTemplate;
        this.messageService = messageService;
    }

    @MessageMapping("/chat.private")
    public void sendPrivateMessage(@Payload Message message) {
        message.setTimestamp(LocalDateTime.now());
        messageService.save(message);
        messagingTemplate.convertAndSendToUser(message.getRecipient(), "/private", message);
    }
}
