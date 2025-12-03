import { OpenRouter } from '@openrouter/sdk';

const client = new OpenRouter({ apiKey: process.env.OPENROUTER_API_KEY });

const stream = await client.chat.send({
  model: 'openai/gpt-4o',
  messages: [{ role: 'user', content: 'Hello!' }],
  stream: true
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || '');
}
