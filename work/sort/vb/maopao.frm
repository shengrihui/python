VERSION 5.00
Begin VB.Form Form1 
   Caption         =   "Form1"
   ClientHeight    =   3735
   ClientLeft      =   60
   ClientTop       =   405
   ClientWidth     =   7920
   LinkTopic       =   "Form1"
   ScaleHeight     =   3735
   ScaleWidth      =   7920
   StartUpPosition =   3  '´°¿ÚÈ±Ê¡
   Begin VB.ListBox List1 
      Height          =   2940
      Left            =   1920
      TabIndex        =   1
      Top             =   120
      Width           =   3975
   End
   Begin VB.CommandButton Command1 
      Caption         =   "Command1"
      Height          =   495
      Left            =   480
      TabIndex        =   0
      Top             =   120
      Width           =   1215
   End
End
Attribute VB_Name = "Form1"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Dim d() As Integer
Dim n As Integer

Private Sub Command1_Click()
    
    Dim i As Integer, j As Integer, t As Integer, c As Long
    Dim st As Date
    List1.Clear
    Randomize
    n = 20000
    ReDim d(1 To n) As Integer
    
    st = Time
    List1.AddItem "before sort:"
    For i = 1 To n
        d(i) = Int(Rnd() * 12345 + 1)
        'List1.AddItem Str(i) + ":" + Str(d(i))
    Next i
  'Ã°ÅÝÉýÐò  Ã°ÅÝ
    For i = 1 To n - 1
        For j = n To i + 1 Step -1
            If d(j) < d(j - 1) Then
                t = d(j): d(j) = d(j - 1): d(j - 1) = t
            End If
        Next j
    Next i
    List1.AddItem "after sort:"
    'For i = 1 To n
     '   List1.AddItem Str(i) + ":" + Str(d(i))
    'Next i
    List1.AddItem Str(Second(Time - st))
End Sub
