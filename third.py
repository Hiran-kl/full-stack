import MessageList from './MessageList';
import MessageForm from './MessageForm';    
import UserInput from './UserInput';
import ConversationHistory from './ConversationHistory';

export default function chatwindow() {
  return (
    <div>
      <ConversationHistory />
      <UserInput />
      <MessageList />
      <MessageForm />
    </div>
  );
}
export { chatwindow };

import {createRoot} from 'react-dom/client';
import React from 'react';
import { chatwindow } from './third';
const container = document.getElementById('chat-window');
const root = createRoot(container);
root.render(<chatwindow />);

const chatWindow = document.getElementById('chat-window');
if (chatWindow) {
  chatWindow.style.display = 'block';
} else {
  console.error('Chat window element not found');
}
