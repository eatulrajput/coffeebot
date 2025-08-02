import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';

type Sender = 'user' | 'bot';

interface Message {
  sender: Sender;
  text: string;
}

const Chat: React.FC = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState<Message[]>([]);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(scrollToBottom, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { sender: 'user', text: input };
    setMessages(prev => [...prev, userMessage]);

    try {
      const response = await axios.post('http://localhost:8000/chat', {
        message: input,
      });

      const botMessage: Message = {
        sender: 'bot',
        text: String(response.data.reply),
      };

      setMessages(prev => [...prev, botMessage]);
    } catch {
      const errorMessage: Message = {
        sender: 'bot',
        text: '⚠️ Error: Could not connect to server.',
      };
      setMessages(prev => [...prev, errorMessage]);
    }

    setInput('');
  };

  return (
    <div className="flex flex-col h-screen bg-gradient-to-tr from-blue-500 to-orange-500 text-white">
      {/* Chat header */}
      <div className="p-4 text-xl font-semibold bg-black/50 shadow">
        Coffee Bot ☕
      </div>

      {/* Chat messages */}
      <div className="flex-1 overflow-y-auto px-4 py-6 space-y-4 bg-gradient-to-tr from-blue-500 to-orange-500">
        {messages.map((msg, index) => (
          <div
            key={index}
            className={`flex w-full ${
              msg.sender === 'user' ? 'justify-end' : 'justify-start'
            }`}
          >
            <div
              className={`max-w-xl whitespace-pre-wrap px-4 py-3 rounded-lg text-lg shadow ${
                msg.sender === 'user'
                  ? 'bg-blue-600 text-white rounded-br-none'
                  : 'bg-blue-600/50 text-white rounded-bl-none'
              }`}
            >
              {msg.text}
            </div>
          </div>
        ))}
        <div ref={messagesEndRef} />
      </div>

      {/* Input field */}
      <div className="bg-black/40 p-4">
        <div className="flex gap-2">
          <input
            type="text"
            placeholder="Type a message..."
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && sendMessage()}
            className="flex-grow px-4 py-2 border bg-black/50 rounded-full focus:outline-none focus:ring focus:bg-blue-950"
          />
          <button
            onClick={sendMessage}
            className="px-5 py-2 bg-blue-600 text-white rounded-full hover:bg-blue-700 transition"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chat;
