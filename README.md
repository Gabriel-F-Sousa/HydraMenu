<p>HydraMenu is a menu module for MicroHydra. In the latest update, <a target="_blank" rel="noopener noreferrer" href="https://github.com/echo-lalia">echo-lalia</a> completely overhauled the code, optimizing it and making it easier to use.<br>&nbsp;</p>
<p>Documentation by <a target="_blank" rel="noopener noreferrer" href="https://github.com/echo-lalia">echo-lalia</a>. I just grouped it into the text below.</p>
<ul>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/Gabriel-F-Sousa/HydraMenu/edit/main/README.md#menuitem">MenuItem</a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/Gabriel-F-Sousa/HydraMenu/edit/main/README.md#BoolItem">BoolItem</a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/Gabriel-F-Sousa/HydraMenu/edit/main/README.md#DoItem">DoItem</a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/Gabriel-F-Sousa/HydraMenu/edit/main/README.md#RGBItem">RGBItem</a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/Gabriel-F-Sousa/HydraMenu/edit/main/README.md#IntItem">IntItem</a></li>
    <li><a target="_blank" rel="noopener noreferrer" href="https://github.com/Gabriel-F-Sousa/HydraMenu/edit/main/README.md#WriteItem">WriteItem</a></li>
</ul>
<h2>MenuItem</h2>
<p>Parent class for HydraMenu Menu Items.</p>
<p>Args shared by every item:</p>
<ul>
    <li>text (str):<ul>
            <li>Display text of the menu item.</li>
        </ul>
    </li>
    <li>value:<ul>
            <li>The value that the menu item controls.</li>
        </ul>
    </li>
    <li>callback (callable):<ul>
            <li>Callback to call when menu item is updated. (optional)</li>
        </ul>
    </li>
    <li>instant_callback (callable):<ul>
            <li>&nbsp;Callback for any time menu item is changed, even before changes are confirmed. (optional)</li>
        </ul>
    </li>
</ul>
<h2>BoolItem</h2>
<p>BoolItems just work as a toggle switch, and return bool</p>
<h2>DoItem</h2>
<p>DoItems are used just for calling a specific callback.</p>
<h2>RGBItem</h2>
<p>This is an item which selects a 16 bit "RGB 565" color. The returned value will be a single integer, representing the color choice.</p>
<h2>IntItem</h2>
<p>IntItems are for creating Integer selection options.&nbsp;</p>
<p>Args:</p>
<ul>
    <li>&nbsp;min_int (int):<ul>
            <li>The minimum allowed value.</li>
        </ul>
    </li>
    <li>max_int (int):<ul>
            <li>The maximum allowed value.</li>
        </ul>
    </li>
</ul>
<h2>WriteItem</h2>
<p>WriteItem allows the user to enter some text. Its value is a string.</p>
<p>Args:</p>
<ul>
    <li>hide (bool):<ul>
            <li>Whether or not to hide the entered text.</li>
        </ul>
    </li>
</ul>
