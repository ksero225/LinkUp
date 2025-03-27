package com.LinkUp.LinkUp.services;

import com.LinkUp.LinkUp.domain.documents.Message;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface MessageService {
    void save(Message message);

    Page<Message> findBySenderAndRecipientOrRecipientAndSender(String sender, String recipient, String recipient1, String sender1, Pageable pageable);
}
