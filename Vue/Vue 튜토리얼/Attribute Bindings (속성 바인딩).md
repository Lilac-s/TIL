# Attribute Bindings (속성 바인딩)



- in Vue, mustaches are only used for text interpolation. To bind an attribute to a dynamic value, we use the `v-bind` directive

- A **directive** is a special attribute that starts with the `v-` prefix. They are part of Vue's template syntax. Similar to text interpolations, directive values are JavaScript expressions that have access to the component's state.

  > v-bind는 태그의 속성을 동적으로 변화할 때 사용한다. 즉, 태그에 여러가지 값이 적용되어야 할 때 사용된다는 뜻이다. 

- The part after the colon (`:id`) is the "argument" of the directive. Here, the element's `id` attribute will be synced with the `dynamicId` property from the component's state.

