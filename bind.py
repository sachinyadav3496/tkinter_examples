import tkinter as tk

def showPosEvent(event):
    print(f"Widget={event.widget} X={event.x} Y={event.y}")

def showAllEvent(event):
    print(event)
    for attr in dir(event):
        if not attr.startswith('__'):
            print(f"{attr} => {getattr(event,attr)}")

def onKeyPressEvent(event):
    print("Got key Press",event.char)

def onArrowKey(event):
    print("Got up Arrow key Pressed")

def onReturnKey(event):
    print("Got return Key Pressed")

def onLeftClick(event):
    print("Got left mouse butoon clicked: ",end=' ')
    showPosEvent(event)

def onRightClick(event):
    print("Got Right Mouse button clicked: ",end=" ")
    showAllEvent(event)

def onMiddleClick(event):
    print("Got middle mouse button clicked: ",end=" ")
    showAllEvent(event)

def onLeftDrag(event):
    print("Got left mouse button drag: ",end=' ')
    showPosEvent(event)

def onDoubleLeftClick(event):
    print("Got double left mouse click: ",end=" ")
    showPosEvent(event)
    tkroot.quit()

tkroot = tk.Tk()

labelfont = ('courier', 20, 'bold')
widget = tk.Label(tkroot, text="Hello Bind World!!")
widget.config(bg="red", font=labelfont)
widget.config(height=5, width=20)
widget.pack(expand=tk.YES, fill=tk.BOTH)


widget.bind("<Button-1>",onLeftClick)
widget.bind("<Button-3>",onRightClick)
widget.bind("<Button-2>",onMiddleClick)
widget.bind("<Double-1>",onDoubleLeftClick)
widget.bind("<B1-Motion>",onLeftDrag)


widget.bind("<KeyPress>",onKeyPressEvent)
widget.bind("<Up>",onArrowKey)
widget.bind("<Return>",onReturnKey)

widget.focus()
tkroot.title("Click Me")
tkroot.mainloop()


"""
Other bind Events
Besides those illustrated in this example, a tkinter script can register to catch additional
kinds of bindable events. For example:
• <ButtonRelease> fires when a button is released (<ButtonPress> is run when the
button first goes down).
• <Motion> is triggered when a mouse pointer is moved.
• <Enter> and <Leave> handlers intercept mouse entry and exit in a window’s display
area (useful for automatically highlighting a widget).
• <Configure> is invoked when the window is resized, repositioned, and so on (e.g.,
the event object’s width and height give the new window size). We’ll make use of
this to resize the display on window resizes in the PyClock example of Chapter 11.
• <Destroy> is invoked when the window widget is destroyed (and differs from the
protocol mechanism for window manager close button presses). Since this interacts with widget quit and destroy methods, I’ll say more about the event later in
this section.
• <FocusIn> and <FocusOut> are run as the widget gains and loses focus.
• <Map> and <Unmap> are run when a window is opened and iconified.
• <Escape>, <BackSpace>, and <Tab> catch other special key presses.
• <Down>, <Left>, and <Right> catch other arrow key presses.
This is not a complete list, and event names can be written with a somewhat sophisticated syntax of their own. For instance:
• Modifiers can be added to event identifiers to make them even more specific; for
instance, <B1-Motion> means moving the mouse with the left button pressed, and
<KeyPress-a> refers to pressing the “a” key only.
• Synonyms can be used for some common event names; for instance, <Button
Press-1>, <Button-1>, and <1> mean a left mouse button press, and <KeyPress-a>
and <Key-a> mean the “a” key. All forms are case sensitive: use <Key-Escape>, not
<KEY-ESCAPE>.
• Virtual event identifiers can be defined within double bracket pairs (e.g., <<Paste
Text>>) to refer to a selection of one or more event sequences.
In the interest of space, though, we’ll defer to other Tk and tkinter reference sources
for an exhaustive list of details on this front. Alternatively, changing some of the settings
in the example script and rerunning can help clarify some event behavior, too; this is
Python, after all.
More on <Destroy> events and the quit and destroy methods
Before we move on, one event merits a few extra words: the <Destroy> event (whose
name is case significant) is run when a widget is being destroyed, as a result of both
Binding Events | 447script method calls and window closures in general, including those at program exit.
If you bind this on a window, it will be triggered once for each widget in the window;
the callback’s event argument widget attribute gives the widget being destroyed, and
you can check this to detect a particular widget’s destruction. If you bind this on a
specific widget instead, it will be triggered once for that widget’s destruction only.
It’s important to know that a widget is in a “half dead” state (Tk’s terminology) when
this event is triggered—it still exists, but most operations on it fail. Because of that, the
<Destroy> event is not intended for GUI activity in general; for instance, checking a text
widget’s changed state or fetching its content in a <Destroy> handler can both fail with
exceptions. In addition, this event’s handler cannot cancel the destruction in general
and resume the GUI; if you wish to intercept and verify or suppress window closes
when a user clicks on a window’s X button, use WM_DELETE_WINDOW in top-level windows’
protocol methods as described earlier in this chapter.
You should also know that running a tkinter widget’s quit method does not trigger any
<Destroy> events on exit, and even leads to a fatal Python error on program exit in 3.X
if any <Destroy> event handlers are registered. Because of this, programs that bind this
event for non-GUI window exit actions should usually call destroy instead of quit to
close, and rely on the fact that a program exits when the last remaining or only Tk root
window (default or explicit) is destroyed as described earlier. This precludes using
quit for immediate shutdowns, though you can still run sys.exit for brute-force exits.
"""
