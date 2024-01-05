# Adding QtCollider widgets

These instructions detail how to add functionality to existing QtCollider widgets (such as TreeView and Knob). Each
widget typically corresponds to a single Qt class, and the simplest way to add functionality is by providing access to
an existing C++ function of the Qt widget.

1. Locate the C++ source for the widget in `/QtCollider/widgets/`.
2. Add the signature for the function in the header file.
3. Add the implementation for the function in the implementation file.
4. Locate the SC source for the widget in `/SCClassLibrary/Common/GUI/Base/`.
5. Add a suitably named new method in the class file that calls down to the QtCollider widget using `invokeMethod`.
6. Document the method in the corresponding schelp file in `/HelpSource/Classes/`.

Technical note: not all types can be transcoded between SuperCollider and QtCollider widgets. However, all primitive
types, some collection types, and a few class types are supported. The code which controls this can be found in
`QtCollider::MetaType::find( PyrSlot * )`.

## Example

[PR #3560](https://github.com/supercollider/supercollider/pull/3560) demonstrates how to do this by adding
`setColumnWidth` to `TreeView`:

1. The C++ files are `/QtCollider/widgets/QcTreeWidget.{cpp,h}`
2. The function signature is:

   ```cpp
   Q_INVOKABLE void setColumnWidth( int column, int width );
   ```

3. The implementation simply calls up to `QTreeView`:

   ```cpp
   void QcTreeWidget::setColumnWidth( int column, int width )
   {
     QTreeWidget::setColumnWidth( column, width );
   }
   ```

4. The SC file is `/SCClassLibrary/Common/GUI/Base/QTreeView.sc`
5. The new method simply forwards arguments to `invokeMethod`:

   ```supercollider
   setColumnWidth { arg column, width;
   	this.invokeMethod( \setColumnWidth, [column, width] )
   }
   ```

6. The documentation is added to `/HelpSource/Classes/TreeView.schelp`:

   ```scdoc
   METHOD:: setColumnWidth
   
   ARGUMENT:: column
      The integer index of the column to modify
   ARGUMENT:: width
      Integer width in pixels
   ```
