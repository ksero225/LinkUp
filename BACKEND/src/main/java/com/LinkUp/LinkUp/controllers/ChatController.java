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
    public void sendPrivateMessage(@Payload Message message){
        System.out.println("SENDING PRIVATE MESSAGE: " + message);
        messagingTemplate.convertAndSendToUser(message.getRecipient(), "/queue/messages", message);
    }

//    @MessageMapping("/chat.register")
//    @SendTo("/topic/public")
//    public Message register(@Payload Message message, SimpMessageHeaderAccessor headerAccessor) {
//        headerAccessor.getSessionAttributes().put("username", message.getSender());
//        return message;
//    }
//
//    @MessageMapping("/chat.send")
//    @SendTo("/topic/public")
//    public Message sendMessage(@Payload Message message) {
//        return message;
//    }
}
