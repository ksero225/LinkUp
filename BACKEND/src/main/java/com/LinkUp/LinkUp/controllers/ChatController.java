package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.Message;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.messaging.handler.annotation.MessageMapping;
import org.springframework.messaging.handler.annotation.Payload;
import org.springframework.messaging.handler.annotation.SendTo;
import org.springframework.messaging.simp.SimpMessageHeaderAccessor;
import org.springframework.messaging.simp.SimpMessagingTemplate;
import org.springframework.stereotype.Controller;

@Controller
public class ChatController {
    SimpMessagingTemplate messagingTemplate;

    public ChatController(SimpMessagingTemplate messagingTemplate) {
        this.messagingTemplate = messagingTemplate;
    }

    @MessageMapping("/chat.private")
    public void sendPrivateMessage(@Payload Message message) {
        System.out.println("MESSAGE RECIPIENT: " + message.getRecipient());
        System.out.println("MESSAGE SENDER: " + message.getSender());

        messagingTemplate.convertAndSendToUser(message.getRecipient(), "/queue/messages", message);
    }
}
