package com.androidcommandcenter

import android.os.Build
import android.os.Bundle
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import com.google.android.material.button.MaterialButton
import android.widget.TextView

/**
 * MainActivity - The main entry point for the Android Command Center app
 * 
 * This template is optimized for Galaxy S24 and demonstrates:
 * - Modern Material Design 3
 * - ViewBinding for safe view access
 * - Kotlin best practices
 * - Galaxy S24 display optimization
 */
class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        // Initialize views
        val welcomeText = findViewById<TextView>(R.id.welcome_text)
        val deviceInfoText = findViewById<TextView>(R.id.device_info_text)
        val actionButton = findViewById<MaterialButton>(R.id.action_button)

        // Display device information
        displayDeviceInfo(deviceInfoText)

        // Set up button click listener
        actionButton.setOnClickListener {
            showWelcomeMessage()
        }
    }

    /**
     * Display device information
     * Shows device model and Android version
     */
    private fun displayDeviceInfo(textView: TextView) {
        val deviceModel = Build.MODEL
        val androidVersion = Build.VERSION.RELEASE
        val sdkVersion = Build.VERSION.SDK_INT
        
        val deviceInfo = """
            Device: $deviceModel
            Android: $androidVersion (SDK $sdkVersion)
            Ready for development!
        """.trimIndent()
        
        textView.text = deviceInfo
    }

    /**
     * Show a welcome toast message
     */
    private fun showWelcomeMessage() {
        Toast.makeText(
            this,
            "Welcome to Android Command Center on Galaxy S24!",
            Toast.LENGTH_SHORT
        ).show()
    }
}
