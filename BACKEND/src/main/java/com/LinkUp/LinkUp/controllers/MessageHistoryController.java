package com.LinkUp.LinkUp.controllers;

import com.LinkUp.LinkUp.domain.documents.Message;
import com.LinkUp.LinkUp.services.MessageService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.data.domain.Sort;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/api/messages")
public class MessageHistoryController {
    private final MessageService messageService;

    public MessageHistoryController(MessageService messageService) {
        this.messageService = messageService;
    }

    @GetMapping
    public Page<Message> getChatHistory(
            @RequestParam String sender,
            @RequestParam String recipient,
            @RequestParam(defaultValue = "0") int page,
            @RequestParam(defaultValue = "20") int size
    ){
        Pageable pageable = PageRequest.of(page, size, Sort.by(Sort.Direction.DESC, "timestamp"));
        return messageService.findBySenderAndRecipientOrRecipientAndSender(sender, recipient, pageable);
    }
}
