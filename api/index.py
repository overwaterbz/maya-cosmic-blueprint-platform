#!/usr/bin/env python3

def handler(event, context):
    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/html'},
        'body': '<h1>Maya Platform - Minimal Test</h1><p>Python function working on Vercel</p>'
    }

# Vercel compatibility
app = handler
