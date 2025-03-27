package com.LinkUp.LinkUp.services.implementations;

import com.LinkUp.LinkUp.domain.documents.Message;
import com.LinkUp.LinkUp.repositories.MessageRepository;
import com.LinkUp.LinkUp.services.MessageService;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.stereotype.Service;

@Service
public class MessageServiceImpl implements MessageService {
    private final MessageRepository messageRepository;

    public MessageServiceImpl(MessageRepository messageRepository) {
        this.messageRepository = messageRepository;
    }

    @Override
    public void save(Message message) {
        messageRepository.save(message);
    }

    @Override
    public Page<Message> findBySenderAndRecipientOrRecipientAndSender(String sender, String recipient, String recipient1, String sender1, Pageable pageable) {
        return messageRepository.findBySenderAndRecipientOrRecipientAndSender(
                sender,
                recipient,
                recipient1,
                sender1,
                pageable
        );
    }
}
