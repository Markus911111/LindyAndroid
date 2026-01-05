# 🤖 Lindy AI Integration Guide

Complete guide to integrating Lindy.ai automation platform with Android Command Center.

## 📋 Table of Contents

1. [What is Lindy?](#what-is-lindy)
2. [Setting Up Lindy](#setting-up-lindy)
3. [Connecting Lindy to Your Project](#connecting-lindy-to-your-project)
4. [Automation Workflows](#automation-workflows)
5. [Lindy API Integration](#lindy-api-integration)
6. [Mobile App Integration](#mobile-app-integration)
7. [Use Cases](#use-cases)
8. [Troubleshooting](#troubleshooting)

## 🎯 What is Lindy?

**Lindy.ai** (https://www.lindy.ai) is an AI-powered automation platform that can:

```
✅ Automate repetitive tasks
✅ Connect multiple services
✅ Process natural language commands
✅ Schedule automated workflows
✅ Integrate with 1000+ apps
✅ Build custom automations
✅ Monitor and alert
```

### Lindy + Android Command Center

```
┌──────────────────────────────────────────────────────────────┐
│              Lindy Integration Architecture                   │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Your Android App                                           │
│         │                                                    │
│         ├─→ Trigger events                                   │
│         │   (Build complete, test pass/fail, etc.)          │
│         │                                                    │
│         ↓                                                    │
│   Lindy.ai Platform                                          │
│         │                                                    │
│         ├─→ Process with AI                                  │
│         ├─→ Execute workflows                                │
│         ├─→ Connect to services                              │
│         │   (GitHub, Slack, Email, etc.)                    │
│         │                                                    │
│         ↓                                                    │
│   Actions                                                    │
│   ├─ Send notifications                                      │
│   ├─ Update documentation                                    │
│   ├─ Create tasks                                            │
│   ├─ Deploy to store                                         │
│   └─ Generate reports                                        │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 🚀 Setting Up Lindy

### Step 1: Create Lindy Account

```
1. Visit: https://www.lindy.ai

2. Click "Get Started" or "Sign Up"

3. Choose sign-up method:
   ├─ Email + Password
   ├─ Google Account (recommended)
   └─ GitHub Account

4. Complete profile setup
   ├─ Name
   ├─ Organization (optional)
   └─ Use case

5. Verify email
   └─ Check inbox for verification link
```

**📷 Screenshot Location**: `docs/images/lindy/01-signup.png`

### Step 2: Create Your First Lindy

```
1. Dashboard → "Create New Lindy"

2. Choose template or start from scratch:
   ├─ "Developer Assistant" (recommended)
   ├─ "Automation Bot"
   └─ "Custom Lindy"

3. Name your Lindy:
   "Android Build Assistant"

4. Configure capabilities:
   [✓] GitHub integration
   [✓] Webhook triggers
   [✓] Email notifications
   [✓] Slack integration (optional)
```

**📷 Screenshot Location**: `docs/images/lindy/02-create-lindy.png`

### Step 3: Get API Credentials

```
1. Lindy Dashboard → Settings → API Keys

2. Click "Create API Key"
   ├─ Name: "AndroidCommandCenter"
   ├─ Permissions: Read/Write
   └─ Expiry: Never (or custom)

3. Copy API Key
   ⚠️  Save securely! Won't show again

4. Copy Webhook URL
   Example: https://hooks.lindy.ai/webhook/abc123def456
```

**📷 Screenshot Location**: `docs/images/lindy/03-api-keys.png`

## 🔗 Connecting Lindy to Your Project

### Method 1: Environment Variables

Create `.env` file in project root:

```bash
# .env (DO NOT COMMIT TO GIT!)

# Lindy Configuration
LINDY_API_KEY=your_api_key_here
LINDY_WEBHOOK_URL=https://hooks.lindy.ai/webhook/your_webhook_id
LINDY_ASSISTANT_ID=assistant_abc123

# Optional: Slack webhook (if using Slack)
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/YOUR/WEBHOOK/URL
```

Add to `.gitignore`:
```bash
echo ".env" >> .gitignore
```

### Method 2: GitHub Secrets

For CI/CD integration:

```
1. GitHub Repository → Settings

2. Secrets and variables → Actions

3. New repository secret:
   ├─ Name: LINDY_API_KEY
   ├─ Value: [paste your API key]
   └─ Add secret

4. Repeat for:
   ├─ LINDY_WEBHOOK_URL
   └─ LINDY_ASSISTANT_ID
```

**📷 Screenshot Location**: `docs/images/lindy/04-github-secrets.png`

### Method 3: Android App (Secure Storage)

```kotlin
// app/src/main/java/com/androidcommandcenter/config/LindyConfig.kt

package com.androidcommandcenter.config

import android.content.Context
import androidx.security.crypto.EncryptedSharedPreferences
import androidx.security.crypto.MasterKey

object LindyConfig {
    private const val PREFS_NAME = "lindy_config"
    private const val KEY_API_KEY = "api_key"
    private const val KEY_WEBHOOK_URL = "webhook_url"
    
    fun saveApiKey(context: Context, apiKey: String) {
        getEncryptedPrefs(context)
            .edit()
            .putString(KEY_API_KEY, apiKey)
            .apply()
    }
    
    fun getApiKey(context: Context): String? {
        return getEncryptedPrefs(context).getString(KEY_API_KEY, null)
    }
    
    fun saveWebhookUrl(context: Context, url: String) {
        getEncryptedPrefs(context)
            .edit()
            .putString(KEY_WEBHOOK_URL, url)
            .apply()
    }
    
    fun getWebhookUrl(context: Context): String? {
        return getEncryptedPrefs(context).getString(KEY_WEBHOOK_URL, null)
    }
    
    private fun getEncryptedPrefs(context: Context) =
        EncryptedSharedPreferences.create(
            context,
            PREFS_NAME,
            MasterKey.Builder(context)
                .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
                .build(),
            EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
            EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM
        )
}
```

Add dependency to `app/build.gradle.kts`:
```kotlin
dependencies {
    // Security
    implementation("androidx.security:security-crypto:1.1.0-alpha06")
}
```

## 🔄 Automation Workflows

### Workflow 1: Build Notification

When Android build completes, notify via Lindy:

```python
# python/automation/lindy_notifier.py

import requests
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

LINDY_WEBHOOK_URL = os.getenv('LINDY_WEBHOOK_URL')

def notify_build_complete(variant: str, success: bool, apk_path: str = None):
    """Notify Lindy about build completion"""
    
    payload = {
        "event": "build_complete",
        "variant": variant,
        "success": success,
        "apk_path": apk_path,
        "timestamp": datetime.now().isoformat(),
        "project": "AndroidCommandCenter"
    }
    
    if success:
        payload["message"] = f"✅ {variant.capitalize()} build successful!"
        if apk_path:
            payload["apk_size"] = Path(apk_path).stat().st_size
    else:
        payload["message"] = f"❌ {variant.capitalize()} build failed!"
    
    try:
        response = requests.post(
            LINDY_WEBHOOK_URL,
            json=payload,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 200:
            print("✅ Lindy notified successfully")
        else:
            print(f"⚠️  Lindy notification failed: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error notifying Lindy: {e}")

def notify_test_results(passed: int, failed: int, total: int):
    """Notify Lindy about test results"""
    
    payload = {
        "event": "test_complete",
        "passed": passed,
        "failed": failed,
        "total": total,
        "success": failed == 0,
        "timestamp": datetime.now().isoformat()
    }
    
    try:
        requests.post(LINDY_WEBHOOK_URL, json=payload, timeout=10)
        print("✅ Test results sent to Lindy")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage
if __name__ == "__main__":
    notify_build_complete(
        variant="debug",
        success=True,
        apk_path="app/build/outputs/apk/debug/app-debug.apk"
    )
```

### Workflow 2: GitHub Integration

Create Lindy workflow to monitor GitHub:

```
Lindy Dashboard → Workflows → Create New

Trigger:
  GitHub Push Event
  Repository: Markus911111/AndroidCommandCenter
  Branch: main

Actions:
  1. Send notification
     "New code pushed to main branch"
  
  2. Wait for GitHub Actions to complete
  
  3. If build successful:
     → Send Slack message
     → Update project board
     → Generate changelog
  
  4. If build failed:
     → Send alert email
     → Create GitHub issue
     → Notify on Slack
```

**📷 Screenshot Location**: `docs/images/lindy/05-github-workflow.png`

### Workflow 3: Scheduled Tasks

```
Lindy Dashboard → Workflows → Schedule

Daily Build Check:
  Schedule: Every day at 2 AM UTC
  
  Actions:
  1. Check GitHub for new commits
  2. If new commits:
     → Trigger build via GitHub Actions API
     → Wait for completion
     → Send summary report
  3. If no commits:
     → Log status
```

### Workflow 4: Smart Deployment

```
Trigger: Manual or on Tag

Conditions:
  - All tests passed
  - Build successful
  - Version bumped

Actions:
  1. Create GitHub release
  2. Upload APK to release
  3. Send to beta testers (via email)
  4. Update documentation
  5. Post to Slack #releases
  6. Tweet announcement (optional)
```

## 🔌 Lindy API Integration

### Python SDK

```python
# python/integrations/lindy_client.py

import requests
import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

class LindyClient:
    """Client for Lindy API"""
    
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv('LINDY_API_KEY')
        self.base_url = "https://api.lindy.ai/v1"
        self.webhook_url = os.getenv('LINDY_WEBHOOK_URL')
        
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
    
    def send_event(self, event_type: str, data: Dict[str, Any]) -> bool:
        """Send event to Lindy webhook"""
        payload = {
            "event": event_type,
            "data": data,
            "source": "AndroidCommandCenter"
        }
        
        try:
            response = self.session.post(self.webhook_url, json=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Error sending event: {e}")
            return False
    
    def ask_assistant(self, question: str) -> Optional[str]:
        """Ask Lindy assistant a question"""
        try:
            response = self.session.post(
                f"{self.base_url}/assistants/ask",
                json={"question": question}
            )
            
            if response.status_code == 200:
                return response.json().get("answer")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def create_task(self, title: str, description: str) -> bool:
        """Create a task via Lindy"""
        payload = {
            "title": title,
            "description": description,
            "project": "AndroidCommandCenter"
        }
        
        return self.send_event("task_created", payload)

# Example usage
if __name__ == "__main__":
    client = LindyClient()
    
    # Send build event
    client.send_event("build_started", {
        "variant": "debug",
        "timestamp": "2024-11-26T14:30:00Z"
    })
    
    # Ask assistant
    answer = client.ask_assistant("What's the current build status?")
    print(f"Lindy says: {answer}")
    
    # Create task
    client.create_task(
        "Update documentation",
        "Add new API integration guide"
    )
```

### Kotlin Integration

```kotlin
// app/src/main/java/com/androidcommandcenter/integrations/LindyClient.kt

package com.androidcommandcenter.integrations

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.json.JSONObject
import java.util.concurrent.TimeUnit

class LindyClient(
    private val apiKey: String,
    private val webhookUrl: String
) {
    private val client = OkHttpClient.Builder()
        .connectTimeout(30, TimeUnit.SECONDS)
        .readTimeout(30, TimeUnit.SECONDS)
        .build()
    
    private val mediaType = "application/json".toMediaType()
    
    suspend fun sendEvent(
        eventType: String,
        data: Map<String, Any>
    ): Boolean = withContext(Dispatchers.IO) {
        try {
            val payload = JSONObject().apply {
                put("event", eventType)
                put("data", JSONObject(data))
                put("source", "AndroidCommandCenter")
            }
            
            val requestBody = payload.toString().toRequestBody(mediaType)
            
            val request = Request.Builder()
                .url(webhookUrl)
                .post(requestBody)
                .addHeader("Content-Type", "application/json")
                .build()
            
            val response = client.newCall(request).execute()
            response.isSuccessful
        } catch (e: Exception) {
            e.printStackTrace()
            false
        }
    }
    
    suspend fun notifyBuildComplete(
        variant: String,
        success: Boolean
    ) = sendEvent(
        "build_complete",
        mapOf(
            "variant" to variant,
            "success" to success,
            "timestamp" to System.currentTimeMillis()
        )
    )
    
    suspend fun notifyAppLaunched() = sendEvent(
        "app_launched",
        mapOf(
            "timestamp" to System.currentTimeMillis()
        )
    )
}

// Usage in MainActivity
class MainActivity : AppCompatActivity() {
    private lateinit var lindyClient: LindyClient
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        
        // Initialize Lindy
        val apiKey = LindyConfig.getApiKey(this) ?: return
        val webhookUrl = LindyConfig.getWebhookUrl(this) ?: return
        
        lindyClient = LindyClient(apiKey, webhookUrl)
        
        // Notify Lindy that app launched
        lifecycleScope.launch {
            lindyClient.notifyAppLaunched()
        }
    }
}
```

Add dependencies to `app/build.gradle.kts`:
```kotlin
dependencies {
    // HTTP client
    implementation("com.squareup.okhttp3:okhttp:4.12.0")
    
    // JSON
    implementation("org.json:json:20231013")
    
    // Coroutines
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.10.1")
}
```

## 📱 Mobile App Integration

### Settings Screen

```kotlin
// app/src/main/java/com/androidcommandcenter/ui/LindySettingsActivity.kt

package com.androidcommandcenter.ui

import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.androidcommandcenter.config.LindyConfig
import com.google.android.material.button.MaterialButton
import com.google.android.material.textfield.TextInputEditText

class LindySettingsActivity : AppCompatActivity() {
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_lindy_settings)
        
        val apiKeyInput = findViewById<TextInputEditText>(R.id.lindy_api_key)
        val webhookInput = findViewById<TextInputEditText>(R.id.lindy_webhook_url)
        val saveButton = findViewById<MaterialButton>(R.id.save_button)
        val testButton = findViewById<MaterialButton>(R.id.test_connection_button)
        
        // Load saved values
        apiKeyInput.setText(LindyConfig.getApiKey(this))
        webhookInput.setText(LindyConfig.getWebhookUrl(this))
        
        saveButton.setOnClickListener {
            val apiKey = apiKeyInput.text.toString()
            val webhookUrl = webhookInput.text.toString()
            
            if (apiKey.isBlank() || webhookUrl.isBlank()) {
                Toast.makeText(this, "Please fill all fields", Toast.LENGTH_SHORT).show()
                return@setOnClickListener
            }
            
            LindyConfig.saveApiKey(this, apiKey)
            LindyConfig.saveWebhookUrl(this, webhookUrl)
            
            Toast.makeText(this, "Saved!", Toast.LENGTH_SHORT).show()
            finish()
        }
        
        testButton.setOnClickListener {
            testConnection()
        }
    }
    
    private fun testConnection() {
        // Test Lindy connection
        Toast.makeText(this, "Testing connection...", Toast.LENGTH_SHORT).show()
        
        val apiKey = findViewById<TextInputEditText>(R.id.lindy_api_key).text.toString()
        val webhookUrl = findViewById<TextInputEditText>(R.id.lindy_webhook_url).text.toString()
        
        if (apiKey.isBlank() || webhookUrl.isBlank()) {
            Toast.makeText(this, "Please fill all fields", Toast.LENGTH_SHORT).show()
            return
        }
        
        lifecycleScope.launch {
            val client = LindyClient(apiKey, webhookUrl)
            val success = client.sendEvent(
                "test_connection",
                mapOf("message" to "Testing from Android Command Center")
            )
            
            runOnUiThread {
                if (success) {
                    Toast.makeText(
                        this@LindySettingsActivity,
                        "✅ Connection successful!",
                        Toast.LENGTH_LONG
                    ).show()
                } else {
                    Toast.makeText(
                        this@LindySettingsActivity,
                        "❌ Connection failed!",
                        Toast.LENGTH_LONG
                    ).show()
                }
            }
        }
    }
}
```

### Layout XML

```xml
<!-- app/src/main/res/layout/activity_lindy_settings.xml -->

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:padding="24dp">

    <TextView
        android:id="@+id/title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Lindy Integration"
        android:textSize="24sp"
        android:textStyle="bold"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintStart_toStartOf="parent" />

    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/api_key_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="32dp"
        android:hint="Lindy API Key"
        app:layout_constraintTop_toBottomOf="@id/title">
        
        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/lindy_api_key"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="textPassword" />
    </com.google.android.material.textfield.TextInputLayout>

    <com.google.android.material.textfield.TextInputLayout
        android:id="@+id/webhook_layout"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        android:hint="Webhook URL"
        app:layout_constraintTop_toBottomOf="@id/api_key_layout">
        
        <com.google.android.material.textfield.TextInputEditText
            android:id="@+id/lindy_webhook_url"
            android:layout_width="match_parent"
            android:layout_height="wrap_content"
            android:inputType="textUri" />
    </com.google.android.material.textfield.TextInputLayout>

    <com.google.android.material.button.MaterialButton
        android:id="@+id/test_connection_button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="24dp"
        android:text="Test Connection"
        style="@style/Widget.Material3.Button.OutlinedButton"
        app:layout_constraintTop_toBottomOf="@id/webhook_layout" />

    <com.google.android.material.button.MaterialButton
        android:id="@+id/save_button"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginTop="16dp"
        android:text="Save"
        app:layout_constraintTop_toBottomOf="@id/test_connection_button" />

    <TextView
        android:id="@+id/help_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="24dp"
        android:text="Get your API key from:\nhttps://www.lindy.ai/settings/api"
        android:textSize="12sp"
        android:textColor="?android:textColorSecondary"
        app:layout_constraintTop_toBottomOf="@id/save_button"
        app:layout_constraintStart_toStartOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

## 💡 Use Cases

### 1. Automated Build Reports

```
When build completes → Lindy:
  ├─ Creates summary report
  ├─ Sends to team via Slack
  ├─ Updates project dashboard
  └─ Logs to analytics
```

### 2. Smart Testing

```
On test failure → Lindy:
  ├─ Analyzes failure logs
  ├─ Creates GitHub issue with details
  ├─ Assigns to relevant developer
  └─ Sends notification
```

### 3. Release Management

```
On version tag → Lindy:
  ├─ Generates changelog
  ├─ Creates GitHub release
  ├─ Uploads APK
  ├─ Sends to beta testers
  └─ Updates documentation
```

### 4. Development Assistant

```
Developer asks Lindy:
  "What's the current build status?"
  "Show me failed tests from today"
  "Deploy latest version to beta"
  "Generate performance report"

Lindy responds with real-time data
```

## 🔍 Troubleshooting

### Issue: Webhook not receiving events

**Solution**:
```python
# Test webhook directly
import requests

response = requests.post(
    "your_webhook_url",
    json={"test": "message"},
    timeout=10
)

print(f"Status: {response.status_code}")
print(f"Response: {response.text}")
```

### Issue: API key invalid

**Solution**:
1. Verify API key in Lindy dashboard
2. Check for extra spaces
3. Regenerate if needed
4. Update in `.env` file

### Issue: Lindy not responding

**Solution**:
1. Check Lindy.ai status page
2. Verify internet connection
3. Check rate limits
4. Review Lindy dashboard logs

## 📚 Resources

- **Lindy Website**: https://www.lindy.ai
- **Lindy Documentation**: https://docs.lindy.ai
- **API Reference**: https://docs.lindy.ai/api
- **Community**: https://community.lindy.ai
- **Support**: support@lindy.ai

## ✅ Lindy Integration Checklist

- [ ] Created Lindy account
- [ ] Set up first Lindy assistant
- [ ] Obtained API credentials
- [ ] Added credentials to project
- [ ] Tested webhook connection
- [ ] Created automation workflows
- [ ] Integrated with Android app
- [ ] Set up build notifications
- [ ] Configured GitHub integration
- [ ] Tested end-to-end automation

---

**Navigation**:  
← [12-PYDROID-GUIDE.md](12-PYDROID-GUIDE.md) | [INDEX.md](INDEX.md) | [14-GOOGLE-AI-STUDIO.md](14-GOOGLE-AI-STUDIO.md) →
